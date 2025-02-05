from Foot import Foot
class Leg:
    def __init__(self, length, width, side):
        self.length = length
        self.width = width
        self.side = side
        self.foot = Foot(10, side)  

    def __str__(self):
        return f"Leg(side={self.side}, length={self.length}, width={self.width}, foot={self.foot})"
