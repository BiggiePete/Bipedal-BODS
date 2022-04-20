from random import Random, random
from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)
while(True):
    kit.servo[1].angle = Random().randrange(0,180)
    sleep(1)