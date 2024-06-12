import cv2
from megapi import *
import time 
#This is about halfway hard-coded. The bot can't yet pick things up, but it can traverse the garden in four stops and 
#diferentiate which function to use depending on our input. 
#The next most important step is to utilize the pincers and figure out how we will maneuver them in order to accomplish
#each function's task.

#We will define all port values up here. For now I've set placeholder values
wheelspeed = 50
limbspeed = 25
port = 1
slot = 1
slot2 = 2
armslot = 3
pincerslot = 4
sensorport = 5
duration = 1
turnduration = 2

def patrol(gardenFunc):
    for i in range(4):
     movedur(slot, wheelspeed, duration)
     turnaround(slot, slot2, duration/4)
     while True:
       match gardenFunc:
            case 0:
             snapshot()
            case 1:
             water()
            case 2:    
             soilquality()
    sleep(5)
    turnaround()
    sleep(3)
    movedur(slot, wheelspeed, 4)
    turnaround(slot, slot2, wheelspeed)
    sleep(3)
    return 0

def water(limbspeed):
    for i in range(5):
       movedur(slot, slot, limbspeed, duration)
       movedur(slot, slot, -limbspeed, duration)
    turnaround(slot2, slot, duration/4)
    return 0




def soilquality(slot, limbspeed):
    movedur(slot, slot, limbspeed, duration)
    sleep(5)
    movedur(slot, slot, -limbspeed, duration)
    turnaround(slot2, slot, duration/4)
    return 0


def snapshot():
    cam = cv2.VideoCapture(0)
    #Not sure how we're going to take a picture
    turnaround(slot2, slot, duration/4)
    return 0


def initialize():
    bot = MegaPi()
    sleep(5)
    #bot.start(serialport)
    return bot

def motor(slot, speed):
    bot.encoderMotorRun(slot, speed)
    return 0

def movedur(slot, slot2, speed, duration):
     motor(slot, speed)
     motor(slot2, speed)
     time.sleep(duration)
     motor(slot, 0)
     motor(slot2, 0)

def turnaround(slot, slot2, speed):
   bot.encoderMotorRun(slot, speed)
   bot.encoderMotorRun(slot2, -speed)
   motor(slot,0)
   motor(slot2,0)


def obstacle(distance):
    if(distance < 5):
        movedur(armslot, armslot, limbspeed, duration/2)
        movedur(pincerslot, pincerslot, limbspeed, duration/2)
        movedur(armslot, armslot, -limbspeed, duration/2)
        return False

def pickup(armslot, pincerslot, sensorport):
    tester = True
    while tester:
            tester = bot.ultrasonicSensorRead(sensorport, obstacle)
            sleep(.5)

def exterior(func):
   patrol(func)
   pickup(armslot, pincerslot, sensorport)
   return 0
#Turn on hardware, set up robot
bot = initialize()
#Snapshots come first
exterior(0)
#Soil quality second
exterior(1)
#Watering last
exterior(2)
#Turn off hardware after it's no longer being used
for i in range(4):
   motor(i, 0)
bot.stop()