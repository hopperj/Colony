import pygame

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


    def update(self):
        pass

    def moveTo(self,x,y):

        self.x = x
        self.y = y

        self.rect.x = x*self.size
        self.rect.y = y*self.size