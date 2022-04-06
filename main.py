from time import sleep
from Walker import Walker as w
from adafruit_servokit import ServoKit as sk
import numpy as np


def init():
    print("Setting all Servos to their resting State")
    kit = sk(channels=16)
    biped = w(kit)

    biped.Reset()
    while True:
        print("w = walk")
        print("s = squat")
        print("r = reset")
        x = input("Command : ")
        if x == "w":
            run(2)
        elif x == "s":
            biped.Squat()
        elif x == "r":
            biped.Reset()
        

def run(s):
    print("Taking " + str(s) + " Steps!")
    # first order of buissiness is to find out how many times we need to move each leg
    l_leg_steps = np.mod(s,2)
    r_leg_steps = l_leg_steps + 1


    # we wil always step with our right leg first
    
    #lets first detect which leg to step with, inside our loop
    while s > 0:
        s-=1
        if r_leg_steps > l_leg_steps:
            #right leg step
            sleep(w.LiftLeg(1))
        else:
            #left leg step
            sleep(w.LiftLeg(0))
        
    
init()