class Servo:

    def __init__(self, Kit, ID, angle=90):
        self.ID = ID
        self.angle = angle
        self.kit = Kit
        return True

    def ChangeAngle(self, angle):
        self.kit.servo[self.ID] = angle
        self.angle = angle

    def CheckAngle(self):
        return self.angle
