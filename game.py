# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE    = (   0, 0,   255)

import pygame
import numpy as np
import random


from Ant import Ant

class Game:


    def __init__(self,sw=800, sh=800):
        self.SCREEN_WIDTH = sw
        self.SCREEN_HEIGHT = sh

        self.screen_size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.grid_size = 5


        self.clock = pygame.time.Clock()

        self.gameMap = np.zeros( (self.SCREEN_WIDTH/self.grid_size, \
                                  self.SCREEN_HEIGHT/self.grid_size) )

        self.done = False
        self.FPS = 60

        self.numberOfAnts = 5
        self.numberOfWallSeeds = 50
        self.wallSpreadProb = 0.75

        self.initScreen()
        
        self.initWalls()
        self.initAnts()


        self.goal = [ self.SCREEN_WIDTH/( 2*self.grid_size ), \
                      self.SCREEN_HEIGHT/( 2*self.grid_size) ]
        #self.seedMap()


        self.mapX = 0
        self.mapY = 0


    def initWalls(self):
        self.walls = pygame.sprite.Group()

        for i in range(self.numberOfWallSeeds):
            x = random.randint( 0, (self.SCREEN_WIDTH/self.grid_size)-1 )
            y = random.randint( 0, (self.SCREEN_HEIGHT/self.grid_size)-1 )           
            try:
                # If there isn't already something there
                if not self.gameMap[x][y]:
                    #Seed the wall
                    self.gameMap[x][y] = 2
                    self.walls.add( Wall( BLACK, x, y, self.grid_size ) )
                    self.spreadWalls(x,y,x,y)
            except IndexError:
                print "Wall:",x,y
                    
    def spreadWalls(self, x, y, x0, y0):

        positions = [ [x, y+1], [x+1, y+1], [x+1, y], \
                      [x+1, y-1], [x, y-1], [x-1, y-1], \
                      [x-1, y], [x-1, y-1] ]

        for x,y in positions:
            if self.isVacant(x,y):
                dist = np.sqrt( (x0-x)**2 + (y0-y)**2 )
                if random.random() < self.wallSpreadProb/dist:
                    self.gameMap[x][y] = 2
                    self.walls.add( Wall( BLACK, x, y, self.grid_size ) )
                    self.spreadWalls(x,y,x0,y0)


    def initAnts(self):
        self.ants = pygame.sprite.Group()
        
        
        for i in range( self.numberOfAnts ):
            for j in range(200):
                # 200 attempt to find a valid place
                x = random.randint( 0, (self.SCREEN_WIDTH/self.grid_size)-1 )
                y = random.randint( 0, (self.SCREEN_HEIGHT/self.grid_size)-1 )
                print x,y
                try:
                    if not self.gameMap[x][y]:
                        # Seed with an ant
                        self.gameMap[x][y] = 1
                        self.ants.add( Ant( RED, x, y, self.grid_size, moveCD=0.5*self.FPS ) )
                        print "Created an Ant!"
                        break
                except IndexError:
                    print x,y
                    print self.gameMap.shape

    def initScreen(self):
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(WHITE)
        pygame.display.set_caption("Colony")

    def seedMap(self):
        
        for i in range( 1000 ):
            x = random.randint( 0, (self.SCREEN_WIDTH/self.grid_size)-1 )
            y = random.randint( 0, (self.SCREEN_HEIGHT/self.grid_size)-1 )
            try:
                if not self.gameMap[x][y]:
                    # Seed with an ant
                    self.gameMap[x][y] = 1
                    self.ants.add( Ant( RED, x, y, self.grid_size ) )
            except IndexError:
                print x,y
                print self.gameMap.shape

                
    def isVacant(self,x,y):
        if x<0 or y<0 or x>=len(self.gameMap) or y>=len(self.gameMap[0]):
            return False
   	if self.gameMap[x][y] == 0:
            # !0 = 1
            return not self.gameMap[x][y]
    	else:
            return False             

    def randomMoveAnt(self, ant):
        if random.random() > 0.0:
            d = random.randint(1,8)
            if d == 1:
                if self.isVacant( ant.x, ant.y+1 ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x,ant.y+1)
            elif d ==2:
                if self.isVacant( ant.x+1, ant.y+1 ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x+1,ant.y+1)
                    self.gameMap[ant.x][ant.y] = 1
            elif d ==3:
                if self.isVacant( ant.x+1, ant.y ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x+1,ant.y)
                    self.gameMap[ant.x][ant.y] = 1
            elif d ==4:
                if self.isVacant( ant.x+1, ant.y-1 ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x+1,ant.y-1)
                    self.gameMap[ant.x][ant.y] = 1
            elif d ==5:
                if self.isVacant( ant.x, ant.y-1 ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x,ant.y-1)
                    self.gameMap[ant.x][ant.y] = 1
            elif d ==6:
                if self.isVacant( ant.x-1, ant.y-1 ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x-1,ant.y-1)
                    self.gameMap[ant.x][ant.y] = 1
            elif d ==7:
                if self.isVacant( ant.x-1, ant.y ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x-1,ant.y)
                    self.gameMap[ant.x][ant.y] = 1
            elif d ==8:
                if self.isVacant( ant.x-1, ant.y+1 ):
                    self.gameMap[ant.x][ant.y] = 0
                    ant.moveTo(ant.x-1,ant.y+1)
                    self.gameMap[ant.x][ant.y] = 1




    def run(self):
        for ant in self.ants:
            # Move if there is no path, and isn't waiting for moving cooldown.
            if ant.targetLocation == []:
                if not ant.moveCDCounter:
                    self.randomMoveAnt( ant )


            else:
                if self.isVacant( ant.path[0] ):
                    ant.moveAlongPath()

        # --- Drawing code should go here
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        #self.screen.fill(WHITE)
        background = self.screen.subsurface((self.mapX,
                                        self.mapY,
                                        200,
                                        200)) # take snapshot of bigmap
        self.screen.blit(background, (0,0))
        self.ants.update()    
        self.walls.update()

        self.ants.draw(self.screen)
        self.walls.draw(self.screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        self.clock.tick(30)





class Wall(pygame.sprite.Sprite):

    def __init__(self, color, x, y, size):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #self.screen = screen
        self.color = color
        self.size = size
    
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x*size
        self.rect.y = y*size
        
        self.x = x
        self.y = y
