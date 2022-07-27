#!/usr/bin/env python

import rospy
# import Jetson.GPIO as GPIO
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
import time

def setupGPIO(p1, p2, p3):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(p1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(p2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(p3, GPIO.OUT, initial=GPIO.LOW)


def callback(msg):
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))


def listner():
    rospy.init_node('drive_car', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__=="__main__":
    try: 
        listner()
        ENA = 40
        IN1 = 36
        IN2 = 38
        setupGPIO(ENA, IN1, IN2)
    except rospy.ROSInterruptException:
        pass
