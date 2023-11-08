from Organism import Organism
from numpy import array
from time import sleep


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

with open("./gen0/org0.txt", "r") as f:
    org = Organism(f.readline(), f.readline(), f.readline(), f.readline())
    print(org.cost(boolMatrixBad))
    print(org.cost(boolMatrixGood))