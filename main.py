from Organism import Organism
from numpy import array
from time import sleep
from PIL.ImageGrab import grab

boolMatrixBad = array([
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [True , False, False, False, False, False, False, False, False, True ]
])

boolMatrixGood = array([
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False for _ in range(10)],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [True , True , False, False, False, False, False, False, False, False],
    [True , True , False, False, False, False, False, False, False, False],
    [True , False, False, False, False, False, False, False, False, True ]
])

sleep(5)

img = array(grab((1080, 800, 1081, 801)))

print(img[0][0][0])
exit()

with open("./gen0/org0.txt", "r") as f:
    org = Organism(f.readline(), f.readline(), f.readline(), f.readline())
    print(org.cost(boolMatrixBad))
    print(org.cost(boolMatrixGood))