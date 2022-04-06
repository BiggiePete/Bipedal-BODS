from time import sleep
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
    
    def LiftLeg(self, r):
        """Lifts a leg

        Args:
            r (Int): Anything > 0 is the right leg

        Returns:
            Int: Number of seconds estimated that it will take for the rotation to finish, it is smart to run these statements inside of a sleep command
        """
        if r > 0:
            #lift right leg
            self.RTHigh.SetAngle(200)
            sleep(0.2)
            self.RShin.SetAngle(270 - self.RTHigh.GetAngle() + 20)
            return 2
        else:
            #lift left leg
            self.LTHigh.SetAngle(200)
            sleep(0.2)
            self.LShin.SetAngle(270 - self.LThigh.GetAngle() + 20)
            return 2

    def StepLeg(self,r):
        """Continues the step of a leg

        Args:
            r (Int): right > 0 or left leg 

        Returns:
            Int: Number of secons to wait for the anim to finish
        """
        if r > 0:
            #step the right leg
            self.RTHigh.SetAngle(150)
            sleep(0.2)
            self.RShin.SetAngle(270 - self.RTHigh.GetAngle())
            return 2
        else:
            #step the left leg
            self.LThigh.SetAngle(150)
            sleep(0.2)
            self.LShin.SetAngle(270 - self.LThigh.GetAngle())
            return 2