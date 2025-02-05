class Foot:
    def __init__(self, length, side):
        self.length = length
        self.side = side
    def __str__(self):
        return f"Feet: {self.side}, {self.length} cm long"