import cv2
from megapi import *

#This is about halfway hard-coded. The bot can't yet pick things up, but it can traverse the garden in four stops and 
#diferentiate which function to use depending on our input. 
#The next most important step is to utilize the pincers and figure out how we will maneuver them in order to accomplish
#each function's task.
#We will define all port values up here. For now I've set a universal port value to 1 just to have something there
motorspeed = 100
port = 1
slot = 1

def patrol(gardenFunc):
    for i in range(4):
     motor(motorspeed)
     while True:
       block = bot.ultrasonicSensorRead(port, obstacle)
       match gardenFunc:
            case 0:
             snapshot()
            case 1:
             water()
            case 2:
             soilquality()
       while block:
           block = bot.ultrasonicSensorRead(port, obstacle)
    block = bot.ultrasonicSensorRead(port, obstacle)
    sleep(5)
    turnaround()
    sleep(3)
    motor(motorspeed)
    block = bot.ultrasonicSensorRead(port, obstacle)
    turnaround(motorspeed)
    sleep(3)
    return 0





def water():

    return 0




def soilquality():

    return 0


def snapshot():
    cam = cv2.VideoCapture(0)
    
    return 0


def initialize():
    bot = MegaPi()
    sleep(5)
    #bot.start(serialport)
    return bot

def motor(speed):
    bot.encoderMotorRun(slot, speed)
    bot.encoderMotorRun(slot, speed)

    return 0

def turnaround(speed):
   bot.encoderMotorRun(slot, speed)
   bot.encoderMotorRun(slot, -speed)


def obstacle(distance):
    if(distance < 5):
        motor(0)

def pickup():
   return 0

#Turn on hardware, set up robot
bot = initialize()
#Snapshots come first
patrol(0)
#Soil quality second
patrol(1)
#Watering last
patrol(2)
#Turn off hardware after it's no longer being used
motor(0)
bot.stop()