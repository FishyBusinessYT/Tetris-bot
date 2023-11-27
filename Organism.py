from PIL.ImageGrab import grab
from numpy import array, rot90, delete, insert
from time import sleep, time
from Interface import click
from Interface import move
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class Organism():
    def __init__(self, holesW:str, buriedW:str, heightW:str, terrainW:str) -> None:
        self.holesW = float(holesW.replace("\n", ""))
        self.buriedW = float(buriedW.replace("\n", ""))
        self.heightW = float(heightW.replace("\n", ""))
        self.terrainW = float(terrainW.replace("\n", ""))

        self.posCosts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def play(self):
        img = [[[0]]]
        while img[0][0][0] != 53:
            img = array(grab((1080, 800, 1081, 801)))
            self.update()
            click(self.posCosts.index(min(self.posCosts))/10+0.1, 1)
    
    def cost(self, boolMatrix, lines):
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
                    buried += 1 if heights[idx1] else 0
                    #buried += layers if heights[idx1] else 0

        terrain += abs(heights[0] - heights[1])
        terrain += abs(heights[-2] - heights[-1])
        idx = 1
        for h in heights[1:-1]:
            terrain += (abs(heights[idx] - heights[idx+1]) + abs(heights[idx] - heights[idx-1]))/2
            idx += 1

        print(buried, height, terrain, heights)
        print(self.buriedW, self.heightW, self.terrainW)

        return sum([buried*self.buriedW, height*self.heightW, terrain*self.terrainW, -lines*2]) #Removed holes*self.holesW from sum
    
    def update(self):
        sleep(0.05)
        self.boolMatrix = array([[False for _ in range(10)] for _ in range(20)])
        for i in range(10):
            move(i/10)
            sleep(0.04)

            image = grab((844, 436, 1103, 955)).convert("L") #Grayscale image of the game
            
            #image.save("a" + str(i) + ".png")

            image = array(image)                             #For working with each pixel

            lines = 0

            for y in range(0, 20):
                for x in range(10):
                    if image[26*y+1][26*x+1] != 0:
                        self.boolMatrix[y][x] = True
                    else:
                        self.boolMatrix[y][x] = False
                if self.boolMatrix[y].all() == True:
                    lines += 1
                    self.boolMatrix = delete(self.boolMatrix, y, axis=0)
                    self.boolMatrix = insert(self.boolMatrix, 0, [False for _ in range(10)], axis=0)
            
            self.posCosts[i] = self.cost(self.boolMatrix, lines)
        #print(self.posCosts)
        #input()
        
    
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