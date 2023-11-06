from Organism import Organism

scores = [0, 0, 0, 0, 0, 0, 0, 0]

#Instance generation
for i in range(8):
    with open("./gen0/org" + str(i) + ".txt", "r+") as f:
        org = Organism(f.readline(), f.readline(), f.readline(), f.readline())
        org.play(0.15)
        scores[i] = str(input("Enter organism score: "))

    
