from TileGen import *

class TileClass():
    def __init__(self,left,down,right,up,img):
        self.colours = [0,0,0,0]
        self.colours[3] = up
        self.colours[0] = left
        self.colours[1] = down
        self.colours[2] = right
        self.img = img
