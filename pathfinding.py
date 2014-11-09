import numpy as np

def getAdjacent(self, x,y):
    return [ [x, y+1], [x+1, y+1], [x+1, y], \
             [x+1, y-1], [x, y-1], [x-1, y-1], \
             [x-1, y], [x-1, y-1] ]

def isVacant(self, gameMap,x,y):
    if x<0 or y<0 or x>=len(gameMap) or y>=len(gameMap[0]):
        return False
    if gameMap[x][y] == 0:
        # !0 = 1
        return not gameMap[x][y]
    else:
        return False   

def getPath(self, gameMap, x0,y0, x1,y1, path=[]):
    
    positions = self.getAdjacent(x0,y0)

    for x,y in positions:

        tmpPath = path + (x,y)

        if (x,y) == (x1,y1):
            return tmpPath

        if self.isVacant( gameMap, x,y ):
            gameMap[x][y] = 999
            ret = self.getPath(gameMode, x,y, x1,y1, tmpPath)
            if ret is not None:
                return ret

        else:
            return None
