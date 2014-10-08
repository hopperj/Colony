import pygame
import numpy as np
import random

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE    = (   0, 0,   255)


class Ant(pygame.sprite.Sprite):
    
    def moveTo(self,x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def __init__(self, color, x, y, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #self.screen = screen
        self.color = color
        self.width = width
        self.height = height
    
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
            
        self.position = (x,y,self.width,self.height)          

    def update(self):
        pass





pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
size = (800, 800)
grid_size = 5
screen = pygame.display.set_mode(size)


# Clear the screen and set the screen background
screen.fill(WHITE)



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
            ants.add( Ant( RED, x*grid_size, y*grid_size, grid_size, grid_size ) )
    except IndexError:
        print x,y
        print gameMap.shape


"""
ant_size = 10
for i in range(500):
    x,y = random.randrange(SCREEN_WIDTH-ant_size), random.randrange(SCREEN_HEIGHT-ant_size)
    ant = Ant(RED, x, y, ant_size, ant_size)
    collisions = pygame.sprite.spritecollide(ant, ants, False)

    while len(collisions):
        x,y = random.randrange(SCREEN_WIDTH-ant_size), random.randrange(SCREEN_HEIGHT-ant_size)
        ant.moveTo(random.randrange(SCREEN_WIDTH-ant_size), random.randrange(SCREEN_HEIGHT-ant_size))
        collisions = pygame.sprite.spritecollide(ant, ants, False)
    ants.add( ant )
"""	
	

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something

    
        buttons = pygame.mouse.get_pressed()
        
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    ants.update()    
    
    ants.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
    
    
    
    
    
pygame.quit()
