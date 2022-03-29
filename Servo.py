class Servo:

    def __init__(self, Kit, ID, angle=90):
        self.ID = ID
        self.angle = angle
        self.kit = Kit
        self.kit.servo[ID].actuation_range = 270
        return True

    def SetAngle(self, angle):
        self.kit.servo[self.ID].angle = angle
        self.angle = angle

    def GetAngle(self):
        return self.angle
