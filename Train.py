from Organism import Organism

#Instance generation
for i in range(8):
    with open("./gen0/org" + str(i) + ".txt", "r") as f:
        org = Organism(f.readline(), f.readline(), f.readline(), f.readline())
        org.play(15)
        org.score = input("Enter organism score: ")
        
