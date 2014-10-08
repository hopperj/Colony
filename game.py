# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE    = (   0, 0,   255)


class Game:


    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800

        self.screen_size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.grid_size = 5
        self.screen = pygame.display.set_mode(size)

        self.screen.fill(WHITE)

        self.clock = pygame.time.Clock()
        self.ants = pygame.sprite.Group()

        self.gameMap = np.zeros( (self.SCREEN_WIDTH/self.grid_size, \
                                  self.SCREEN_HEIGHT/self.grid_size) )

        


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
