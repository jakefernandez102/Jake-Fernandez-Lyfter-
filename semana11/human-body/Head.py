class Head:
    def __init__(self, eye_color, hair_color, has_facial_hair):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.has_facial_hair = has_facial_hair

    def __str__(self):
        return f"Head(eye_color={self.eye_color}, hair_color={self.hair_color}, facial_hair={self.has_facial_hair})"
