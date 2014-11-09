import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE    = (   0, 0,   255)


class Ant(pygame.sprite.Sprite):

    def __init__(self, color, x, y, size, job="worker", moveCD=15):
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

        self.job = job

        self.targetLocation = []
        self.path = []

        self.moveCD = moveCD
        self.moveCDCounter = 0


    """
    def moveTo(self,x=0, y=0):
        self.rect.x = x
        self.rect.y = y
    """

    def update(self):
        if self.moveCDCounter > 0:
            self.moveCDCounter -= 1



    def moveAlongPath(self):

        # Temp variables for the new x,y coordinates
        x = self.path[0][0]
        y = self.path[0][1]


        # Set the tolken location
        self.x = x
        self.y = y

        # Update the rectangle
        self.rect.x = x*self.size
        self.rect.y = y*self.size

        # Delete this path position as we are already there.
        del self.path[0]
        self.moveCDCounter = self.moveCD

    def moveTo(self,x,y):

        self.x = x
        self.y = y

        self.rect.x = x*self.size
        self.rect.y = y*self.size
        self.moveCDCounter = self.moveCD
