from random import randint as r

for i in range(8):
    with open("./gen0/org" + str(i) + ".txt", "w") as f:
        f.write(str(r(10, 100)/10) + "\n")
        f.write(str(r(10, 100)/10) + "\n")
        f.write(str(r(10, 100)/10) + "\n")
        f.write(str(r(10, 100)/10) + "\n")