from PIL.ImageGrab import grab
from numpy import array
from time import sleep
from Interface import click
from Interface import move
from Cost import cost

#Game screen starts at (573, 396), ends at (1373, 996)
#Board corner at square 271, 40
#First square at 283, 52
#Adjacent squares +26 pixels
#Will read from row #13 down (bottom 8 rows)

#Next piece position checks:
#671, 137
#671, 150
#658, 150

#Grayscale codes:
#1- Line: 127
#2- Box: 167
#3- S: 126
#4- Z: 63
#5- J: 96
#6- L: 144
#7- T: 72

#Held piece position checks:
#157, 137
#157, 150
#144, 150

boolMatrix = array([[False for _ in range(10)] for _ in range(20)])
heldPiece = 0           #Piece n# divided by 7
nextPiece = 0           #Piece n# divided by 7
currentPiece = 0        #Piece n# divided by 7
previousHeldPiece = 0   #Piece n# divided by 7
posCosts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def update() -> None:
    global boolMatrix, heldPiece, nextPiece, currentPiece, previousHeldPiece
    for i in range(10):
        sleep(0.1)
        move(i/10)

        image = grab((844, 436, 1103, 955)).convert("L") #Grayscale image of the game
        image.save("a" + str(i) + ".png")

        image = array(image)                             #For working with each pixel
        for y in range(12, 20):
            for x in range(10):
                if image[26*y+1][26*x+1] != 0:
                    boolMatrix[y][x] = True
        
        posCosts[i] = cost(boolMatrix)
    
    click(posCosts.index(min(posCosts))/10+0.1, 1)
