from Hand import Hand
class Arm:
    def __init__(self, length, side):
        self.length = length
        self.side = side
        self.hand = Hand(5, side)  # Each arm has one hand

    def __str__(self):
        return f"Arm(side={self.side}, length={self.length}, hand={self.hand})"
