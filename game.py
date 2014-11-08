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
        

        self.initScreen()
        self.initAnts()

        self.seedMap()


    def initAnts(self):
        self.ants = pygame.sprite.Group()
        
        
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
            return not self.gameMap[x][y]
    	else:
            return False             



    def run(self):
        for ant in self.ants:
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



        # --- Drawing code should go here
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self.screen.fill(WHITE)

        self.ants.update()    

        self.ants.draw(self.screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        self.clock.tick(60)
