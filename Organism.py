from PIL.ImageGrab import grab
from numpy import array
from time import sleep
from Interface import click
from Interface import move
from Cost import cost

class Organism():
    def __init__(self, holesW:int, buriedW:int, heightW:int, terrainW:int) -> None:
        self.holesW = holesW
        self.buriedW = buriedW
        self.heightW = heightW
        self.terrainW = terrainW
