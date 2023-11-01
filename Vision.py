from PIL.ImageGrab import grab
from numpy import array
from time import sleep
from Interface import click

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


def update(i) -> None:
    global boolMatrix, heldPiece, nextPiece, currentPiece, previousHeldPiece
    image = grab((573, 396, 1373, 996)).convert("L") #Grayscale image of the game
    
    image.save("a" + i + ".png")

    image = array(image)                             #For working with each pixel

    currentPiece = nextPiece

    heldPiece = max(image[137][157], image[150][157], image[150][144])
    heldPiece = [36, 127, 167, 126, 63, 96, 144, 72].index(heldPiece) / 7

    if previousHeldPiece != heldPiece and previousHeldPiece != 0:
        currentPiece = previousHeldPiece

    nextPiece = max(image[137][671], image[150][671], image[150][658])
    nextPiece = [36, 127, 167, 126, 63, 96, 144, 72].index(nextPiece) / 7
    previousHeldPiece = heldPiece


    for y in range(12, 20):
        for x in range(10):
            if image[52 + 26*y][283 + 26*x] != 0:
                boolMatrix[y][x] = True

sleep(4)

pieces = {
    0/7: "None",
    1/7: "Line",
    2/7: "Box",
    3/7: "S",
    4/7: "Z",
    5/7: "J",
    6/7: "L",
    7/7: "T"
}

for i in range(10):
    click(0.5, i%2)
    sleep(0.1)
    update(str(i))

    print(boolMatrix)
    print("Held:", pieces[heldPiece])
    print("Next:", pieces[nextPiece])
    print("Current:", pieces[currentPiece])
    print()