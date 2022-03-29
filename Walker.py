from Servo import Servo


class Walker:
    def __init__(self, kit) -> None:
        self.kit = kit

        self.LHip = Servo(kit, 0)
        self.RHip = Servo(kit, 1)

        self.LThigh = Servo(kit, 3)
        self.RTHigh = Servo(kit, 4)

        self.LShin = Servo(kit, 6)
        self.RShin = Servo(kit, 7)

        self.All = [self.LHip,self.LThigh,self.LShin,self.RHip,self.RTHigh,self.RShin]

        self.Reset()

    def SetAllServos(self, angle):
        for servo in self.All:
            servo.SetAngle(angle)

    def Reset(self):
        """This will be Eventually Updated to Reset the Servos to the Standing Position
        Right now, the servos will just return to their "Centered" Position
        """
        self.SetAllServos(90)

    def Squat(self):
        pass
