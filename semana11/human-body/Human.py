from Head import Head
from Torso import Torso
from Arm import Arm
from Leg import Leg
class HumanBody:
    def __init__(self, eye_color, hair_color, has_facial_hair):
        self.head = Head(eye_color, hair_color, has_facial_hair)
        self.torso = Torso(40, 80)  

        self.left_arm = Arm(30, "Left")
        self.right_arm = Arm(30, "Right")
        self.left_leg = Leg(40, 10, "Left")
        self.right_leg = Leg(40, 10, "Right")

    def __str__(self):
        return f"""HumanBody:
        {self.head}
        {self.torso}
        {self.left_arm}
        {self.right_arm}
        {self.left_leg}
        {self.right_leg}
        """
