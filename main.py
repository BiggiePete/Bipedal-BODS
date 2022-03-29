from Walker import Walker as w
from adafruit_servokit import ServoKit as sk
import numpy as np


def init():
    print("Setting all Servos to their resting State")
    kit = sk(channels=16)
    biped = w(kit)
    
init()