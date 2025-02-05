class Hand:
    def __init__(self, fingers,side):
        self.fingers = fingers
        self.side = side
        
    def __str__(self):
        return f"Hand: {self.fingers} fingers, {self.side}"