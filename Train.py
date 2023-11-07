from Organism import Organism
from random import randint as r
from time import sleep
from Interface import restart

scores = [0, 0, 0, 0, 0, 0, 0, 0]

def copy_file(path1, path2):
    with open(path1, "r") as f1:
        with open(path2, "w") as f2:
            f2.write(f1.read())

def offspring(path1, path2, n):
    if path1 == "rand":
        with open("./gen1/org" + str(n) + ".txt", "w") as offspring:
            for x in range(4):
                offspring.write(str(r(1, 20)/10) + "\n")
        return

    p = [open(path1, "r").readlines(), open(path2, "r").readlines()]
    with open("./gen1/org" + str(n) + ".txt", "w") as offspring:
        for x in range(4):
            offspring.write(p[r(0, 1)][x])

i = 0
while i < 50:
    i += 1
    for i in range(8):
        sleep(5)
        with open("./gen0/org" + str(i) + ".txt", "r+") as f:
            org = Organism(f.readline(), f.readline(), f.readline(), f.readline())
            org.play(0.5)
            scores[i] = org.get_score()
        restart()

    elite1 = scores.index(sorted(scores)[-1])
    elite2 = scores.index(sorted(scores)[-2])

    copy_file("./gen0/org" + str(elite1) + ".txt", "./gen1/org0.txt")
    copy_file("./gen0/org" + str(elite2) + ".txt", "./gen1/org1.txt")
    offspring("./gen0/org" + str(elite1) + ".txt", "./gen0/org" + str(elite2) + ".txt", 2)
    offspring("./gen0/org" + str(elite1) + ".txt", "./gen0/org" + str(elite2) + ".txt", 3)
    offspring("rand", "", 6)
    offspring("rand", "", 7)

    offspring(
        "./gen0/org" + str(scores.index(sorted(scores)[r(0, 6)])) + ".txt",
        "./gen0/org" + str(scores.index(sorted(scores)[r(0, 6)])) + ".txt",
        4)
    offspring(
        "./gen0/org" + str(scores.index(sorted(scores)[r(0, 6)])) + ".txt",
        "./gen0/org" + str(scores.index(sorted(scores)[r(0, 6)])) + ".txt",
        5)

    for i in range(8):
        copy_file("./gen1/org" + str(i) + ".txt", "./gen0/org" + str(i) + ".txt")
