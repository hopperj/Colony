import pygame
import numpy as np
import random
from game import *
from Ant import Ant







pygame.init()

game = Game()

done = False
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


        game.Config.scrollx = 0
        game.Config.scrolly = 0

        pressedkeys = pygame.key.get_pressed()

        if pressedkeys[pygame.K_LEFT]:
             game.Config.scrollx -= game.Config.scrollstepx
        if pressedkeys[pygame.K_RIGHT]:
             game.Config.scrollx += game.Config.scrollstepx
        if pressedkeys[pygame.K_UP]:
             game.Config.scrolly -= game.Config.scrollstepy
        if pressedkeys[pygame.K_DOWN]:
             game.Config.scrolly += game.Config.scrollstepy

        game.Config.mapX += game.Config.scrollx
        game.Config.mapY += game.Config.scrolly

        if game.Config.mapX <= 0:
            game.Config.mapX = 0
            game.Config.scrollx = 0
        elif game.Config.mapX >= game.Config.bigmapwidth - game.Config.width:
            game.Config.mapX = game.Config.bigmapwidth - game.Config.width
            game.Config.scrollx = 0
        if game.Config.mapY <= 0:
            game.Config.mapY = 0
            game.Config.scrolly = 0
        elif game.Config.mapY >= game.Config.bigmapheight - game.Config.height:
            game.Config.mapY = game.Config.bigmapheight - game.Config.height
            game.Config.scrolly = 0



        



    game.run()
    
    
    

    
    
pygame.quit()
