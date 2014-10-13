import pygame
import numpy as np
import random
import game
import Ant








pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
size = (800, 800)
grid_size = 5
screen = pygame.display.set_mode(size)


# Clear the screen and set the screen background
screen.fill(game.WHITE)



pygame.display.set_caption("Colony")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
ants = pygame.sprite.Group()

gameMap = np.zeros( (SCREEN_WIDTH/grid_size, SCREEN_HEIGHT/grid_size) )
screen = pygame.display.set_mode(size)

for i in range( 1000 ):
    x = random.randint( 0, (SCREEN_WIDTH/grid_size)-1 )
    y = random.randint( 0, (SCREEN_HEIGHT/grid_size)-1 )
    try:
        if not gameMap[x][y]:
            # Seed with an ant
            gameMap[x][y] = 1
            ants.add( Ant( game.RED, x, y, grid_size ) )
    except IndexError:
        print x,y
        print gameMap.shape





def isVacant(x,y):
    if x < len(gameMap) and y < len(gameMap[0]):
        return not gameMap[x][y]
    else:
        return False


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something

    
        buttons = pygame.mouse.get_pressed()
        
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    for ant in ants:
        if random.random() > 0.0:
            d = random.randint(1,8)
            if d == 1:
                if isVacant( ant.x, ant.y+1 ):
                    ant.moveTo(ant.x,ant.y+1)
            elif d ==2:
                if isVacant( ant.x+1, ant.y+1 ):
                    ant.moveTo(ant.x+1,ant.y+1)
            elif d ==3:
                if isVacant( ant.x+1, ant.y ):
                    ant.moveTo(ant.x+1,ant.y)
            elif d ==4:
                if isVacant( ant.x+1, ant.y-1 ):
                    ant.moveTo(ant.x+1,ant.y-1)
            elif d ==5:
                if isVacant( ant.x, ant.y-1 ):
                    ant.moveTo(ant.x,ant.y-1)
            elif d ==6:
                if isVacant( ant.x-1, ant.y-1 ):
                    ant.moveTo(ant.x-1,ant.y-1)
            elif d ==7:
                if isVacant( ant.x-1, ant.y ):
                    ant.moveTo(ant.x-1,ant.y)
            elif d ==8:
                if isVacant( ant.x-1, ant.y+1 ):
                    ant.moveTo(ant.x-1,ant.y+1)
                


    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    ants.update()    
    
    ants.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(10)

    
    
    
    
    
    
pygame.quit()
