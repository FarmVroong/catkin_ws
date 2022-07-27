#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
import time

def setupGPIO(p1, p2, p3):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(p1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(p2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(p3, GPIO.OUT, initial=GPIO.LOW)

def callback():
    rospy.loginfo("Initializing..........")
    ENB_steering = 40
    IN1_steering = 36
    IN2_steering = 38

    ENA_reerleft = 37
    IN1_reerleft = 35
    IN2_reerleft = 33

    ENB_reerright = 19
    IN1_reerright = 21
    IN2_reerleft = 23

    setupGPIO(ENB_steering, IN1_steering, IN2_steering)
    setupGPIO(ENA_reerleft, IN1_reerleft, IN2_reerleft)
    setupGPIO(ENB_reerright, IN1_reerright, IN2_reerleft)

    GPIO.output(ENB_steering, GPIO.LOW)
    GPIO.output(IN1_steering, GPIO.LOW)
    GPIO.output(IN2_steering, GPIO.LOW)
    GPIO.output(ENA_reerleft, GPIO.LOW)
    GPIO.output(IN1_reerleft, GPIO.LOW)
    GPIO.output(IN2_reerleft, GPIO.LOW)
    GPIO.output(ENB_reerright, GPIO.LOW)
    GPIO.output(ENB_reerright, GPIO.LOW)
    GPIO.output(ENB_reerright, GPIO.LOW)
    time.sleep(2)


def listner():
    rospy.init_node('initialize', anonymous=True)
    rospy.spin()


if __name__=="__main__":
    try: 
        listner()
    except rospy.ROSInterruptException:
        pass