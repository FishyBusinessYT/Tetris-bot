from PIL.ImageGrab import grab
from numpy import array, rot90, delete, insert
from time import sleep, time
from Interface import click
from Interface import move
from Cost import cost
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
            layers = 0
            for idx, row in enumerate(column):
                if row:
                    heights[idx1] = 20-idx if not heights[idx1] else heights[idx1]
                    layers += 1
                else:
                    buried += layers if heights[idx1] else 0

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
            move(0.1 + i/10)

            image = grab((844, 436, 1103, 955)).convert("L") #Grayscale image of the game
            #image.save("a" + str(i) + ".png")

            image = array(image)                             #For working with each pixel

            for y in range(3, 20):
                for x in range(10):
                    if image[26*y+1][26*x+1] != 0:
                        try:
                            self.boolMatrix[y][x] = True
                        except TypeError:
                            print(self.boolMatrix)
                    else:
                        self.boolMatrix[y][x] = False
                if self.boolMatrix[y].all() == True:
                    self.boolMatrix = delete(self.boolMatrix, y, axis=0)
                    self.boolMatrix = insert(self.boolMatrix, 0, [False for _ in range(10)], axis=0)
            
            self.posCosts[i] = cost(self.boolMatrix)
    
    def get_score(self):
        img = grab((656, 775, 777, 802))
        score = 0
        while True:
            try:
                score = int(score)
                break
            except ValueError:
                score = pytesseract.image_to_string(img, config='--psm 6 -c tessedit_char_whitelist=0123456789')
        return int(score)