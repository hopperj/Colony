import pygame
import numpy as np
import random
from game import *
from Ant import Ant







pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

game = Game(sw=SCREEN_WIDTH,sh=SCREEN_HEIGHT)

done = False
mapY = 0
mapX = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something

        buttons = pygame.mouse.get_pressed()
        
        if event.type == pygame.QUIT: # If user clicked close
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print "Quitting!"            
            done = True
            break
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            game.mapY -= 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            game.mapY += 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            game.mapX -= 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            game.mapX += 5


        



    game.run()
    
    
    

    
    
pygame.quit()
