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
from Config import Config


class Game:


    def __init__(self):

        self.Config = Config()



        self.clock = pygame.time.Clock()

        self.gameMap = np.zeros( (self.Config.bigmapwidth/self.Config.grid_size, \
                                  self.Config.bigmapwidth/self.Config.grid_size) )

        self.done = False

        self.numberOfAnts = 5
        self.numberOfWallSeeds = 50
        self.wallSpreadProb = 0.75

        self.initScreen()
        
        self.initWalls()
        self.initAnts()


        self.goal = [ self.Config.bigmapwidth/( 2*self.Config.grid_size ), \
                      self.Config.bigmapheight/( 2*self.Config.grid_size) ]
        #self.seedMap()



    def initWalls(self):
        self.walls = pygame.sprite.Group()

        for i in range(self.numberOfWallSeeds):
            x = random.randint( 0, (self.Config.bigmapwidth/self.Config.grid_size)-1 )
            y = random.randint( 0, (self.Config.bigmapheight/self.Config.grid_size)-1 )           
            try:
                # If there isn't already something there
                if not self.gameMap[x][y]:
                    #Seed the wall
                    self.gameMap[x][y] = 2
                    self.walls.add( Wall( BLACK, x, y, self.Config.grid_size ) )
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
                    self.walls.add( Wall( BLACK, x, y, self.Config.grid_size ) )
                    self.spreadWalls(x,y,x0,y0)


    def initAnts(self):
        self.ants = pygame.sprite.Group()
        
        
        for i in range( self.numberOfAnts ):
            for j in range(200):
                # 200 attempt to find a valid place
                x = random.randint( 0, (self.Config.bigmapwidth/self.Config.grid_size)-1 )
                y = random.randint( 0, (self.Config.bigmapheight/self.Config.grid_size)-1 )
                print x,y
                try:
                    if not self.gameMap[x][y]:
                        # Seed with an ant
                        self.gameMap[x][y] = 1
                        self.ants.add( Ant( RED, x, y, self.Config.grid_size, moveCD=0.5*self.Config.FPS ) )
                        print "Created an Ant!"
                        break
                except IndexError:
                    print x,y
                    print self.gameMap.shape

    def initScreen(self):


        self.screen=pygame.display.set_mode((self.Config.width,self.Config.height)) 
        # note that "map" is an pygame function and can not be used as a name for a variable
        self.bigmap = pygame.Surface((self.Config.bigmapwidth, self.Config.bigmapheight))
        # ----------------- create bigmap -------------------
        self.bigmap.fill((128,128,128)) # fill grey




        # paint a grid of dark lines
        for x in range(0,self.Config.bigmapwidth,self.Config.bigmapwidth/self.Config.xtiles): #start, stop, step
            pygame.draw.line(self.bigmap, (64,64,64), (x,0), (x,self.Config.bigmapheight))
        for y in range(0,self.Config.bigmapheight,self.Config.bigmapheight/self.Config.ytiles): #start, stop, step
            pygame.draw.line(self.bigmap, (64,64,64), (0,y), (self.Config.bigmapwidth,y))
        pygame.draw.rect(self.bigmap, (255,0,0), (0,0,self.Config.bigmapwidth, self.Config.bigmapheight), 25) # red bigmap edge
        # paint thin red cross in the middle of the map
        pygame.draw.line(self.bigmap, (200,0,0), (self.Config.bigmapwidth /2, 0),( self.Config.bigmapwidth / 2, self.Config.bigmapheight),1)
        pygame.draw.line(self.bigmap, (200,0,0), (0, self.Config.bigmapheight/2),( self.Config.bigmapwidth , self.Config.bigmapheight/2),1)






        self.bigmap = self.bigmap.convert()
        # ------- background is a subsurface of bigmap ----------
        self.background = pygame.Surface((self.screen.get_size()))
        self.backgroundrect = self.background.get_rect()
        self.background = self.bigmap.subsurface((self.Config.mapX,
                                        self.Config.mapY,
                                        self.Config.width,
                                        self.Config.height)) # take snapshot of bigmap
        # -----------------------------------
        self.background = self.background.convert()
        self.screen.blit(self.background, (0,0)) # delete all


        self.allgroup = pygame.sprite.LayeredUpdates()

        """
        self.screen = pygame.display.set_mode(self.screen_size)
        self.bigMap = pygame.Surface( (1600,1600) )
        self.bigMap.fill( WHITE )
        self.bigMap.convert()


        self.background = pygame.Surface( ( self.screen.get_size() ))
        self.backgroundRect = self.background.get_rect()
        self.background = self.bigMap.subsurface(( 0,0, 400, 400 ))
        
        self.background = self.background.convert()
        self.screen.blit( self.background, (0,0) )
        """



        pygame.display.set_caption("Colony")


    def seedMap(self):
        
        for i in range( 1000 ):
            x = random.randint( 0, (self.Config.bigmapwidth/self.Config.grid_size)-1 )
            y = random.randint( 0, (self.Config.bigmapheight/self.Config.grid_size)-1 )
            try:
                if not self.gameMap[x][y]:
                    # Seed with an ant
                    self.gameMap[x][y] = 1
                    self.ants.add( Ant( RED, x, y, self.Config.grid_size ) )
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
        self.screen.fill(WHITE)
        if self.Config.scrollx == 0 and self.Config.scrolly == 0:
            self.allgroup.clear( self.screen, self.background )
        else:
            #self.Config.mapX = self.Config.scrollx
            #self.Config.mapY = self.Config.scrolly
            print self.Config.mapX,self.Config.mapY, self.Config.width, self.Config.height, self.Config.bigmapwidth, self.Config.bigmapheight
            self.background = self.bigmap.subsurface((self.Config.mapX,
                                                        self.Config.mapY,
                                                        self.Config.width,
                                                        self.Config.height)) # take snapshot of bigmap
            self.screen.blit( self.background, (0,0))

        self.ants.update()    
        self.walls.update()

        self.ants.draw(self.screen)
        self.walls.draw(self.screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        self.clock.tick( self.Config.FPS )





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
