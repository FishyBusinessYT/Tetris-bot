from numpy import rot90

holesW = 1
buriedW = 1
heightW = 1
terrainW = 1

def cost(boolMatrix):
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
        for idx, row in enumerate(column):
            heights[idx1] = 20-idx if row and not heights[idx1] else heights[idx1]
            buried += int(not row) if heights[idx1] else 0

    terrain += abs(heights[0] - heights[1])
    terrain += abs(heights[-2] - heights[-1])
    idx = 1
    for h in heights[1:-1]:
        terrain += (abs(heights[idx] - heights[idx+1]) + abs(heights[idx] - heights[idx-1]))/2
        idx += 1

    return sum(holes*holesW, buried*buriedW, height*heightW, terrain*terrainW)
