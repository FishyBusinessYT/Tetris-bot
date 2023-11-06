from PIL.ImageGrab import grab
from numpy import array, rot90
from time import sleep, time
from Interface import click
from Interface import move
from Cost import cost

class Organism():
    def __init__(self, holesW:int, buriedW:int, heightW:int, terrainW:int) -> None:
        self.holesW = holesW
        self.buriedW = buriedW
        self.heightW = heightW
        self.terrainW = terrainW

        self.heldPiece = 0           #Piece n# divided by 7
        self.nextPiece = 0           #Piece n# divided by 7
        self.currentPiece = 0        #Piece n# divided by 7
        self.previousHeldPiece = 0   #Piece n# divided by 7
        self.posCosts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def play(self, minutes):
        start = time()
        while time()-start < minutes*60:
            self.update()

            click(self.posCosts.index(min(self.posCosts))/10+0.1, 1)
    
    def cost(self, boolMatrix):
        holes = 0
        buried = 0
        height = 0
        terrain = 0

        heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for idx, row in enumerate(boolMatrix):
            if True in row:
                height = 20-idx if not height else height
                for column in row:
                    holes += int(not column)

        for idx1, column in enumerate(rot90(boolMatrix)):
            for idx, row in enumerate(column):
                heights[idx1] = 20-idx if row and not heights[idx1] else heights[idx1]
                buried += int(not row) if heights[idx1] else 0

        terrain += abs(heights[0] - heights[1])
        terrain += abs(heights[-2] - heights[-1])
        idx = 1
        for h in heights[1:-1]:
            terrain += (abs(heights[idx] - heights[idx+1]) + abs(heights[idx] - heights[idx-1]))/2
            idx += 1

        return sum([holes*self.holesW, buried*self.buriedW, height*self.heightW, terrain*self.terrainW])
    
    def update(self):
        self.boolMatrix = array([[False for _ in range(10)] for _ in range(20)])
        for i in range(10):
            sleep(0.05)
            move(i/10)

            image = grab((844, 436, 1103, 955)).convert("L") #Grayscale image of the game
            #image.save("a" + str(i) + ".png")

            image = array(image)                             #For working with each pixel
            for y in range(6, 20):
                for x in range(10):
                    if image[26*y+1][26*x+1] != 0:
                        self.boolMatrix[y][x] = True
                    else:
                        self.boolMatrix[y][x] = False
            
            self.posCosts[i] = cost(self.boolMatrix)