#!/usr/bin/env python

import rospy
# import Jetson.GPIO as GPIO
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
import time

throttle_steering = 0.1
throttle_reer = 0.1

def setupGPIO(p1, p2, p3):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(p1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(p2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(p3, GPIO.OUT, initial=GPIO.LOW)


def callback(msg):
    rate = rospy.Rate(1)
    # rospy.loginfo("Received a /cmd_vel message!")
    # rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    # rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

    ENB_steering = 40
    IN1_steering = 36
    IN2_steering = 38

    ENA_reerleft = 19
    IN1_reerleft = 21
    IN2_reerleft = 23

    ENB_reerright = 37
    IN1_reerright = 33
    IN2_reerright = 35
    
    setupGPIO(ENB_steering, IN1_steering, IN2_steering)
    setupGPIO(ENA_reerleft, IN1_reerleft, IN2_reerleft)
    setupGPIO(ENB_reerright, IN1_reerright, IN2_reerright)


    if (msg.linear.x < 1.1 and msg.linear.x > 0.9 and msg.angular.z > -0.1 and msg.angular.z < 0.1): # straight
        rospy.loginfo("straight")
        GPIO.output(ENA_reerleft, GPIO.HIGH)
        GPIO.output(IN1_reerleft, GPIO.HIGH)
        GPIO.output(IN2_reerleft, GPIO.LOW)
        GPIO.output(ENB_reerright, GPIO.HIGH)
        GPIO.output(IN1_reerright, GPIO.HIGH)
        GPIO.output(IN2_reerright, GPIO.LOW)
        time.sleep(throttle_reer)

    if (msg.linear.x > 0.0 and msg.angular.z > 0.0): # left straight
        rospy.loginfo("left straight")
        GPIO.output(ENB_steering, GPIO.HIGH)
        GPIO.output(IN1_steering, GPIO.HIGH)
        GPIO.output(IN2_steering, GPIO.LOW)
        # time.sleep(throttle_steering)

        GPIO.output(ENA_reerleft, GPIO.HIGH)
        GPIO.output(IN1_reerleft, GPIO.HIGH)
        GPIO.output(IN2_reerleft, GPIO.LOW)

        GPIO.output(ENB_reerright, GPIO.HIGH)
        GPIO.output(IN1_reerright, GPIO.HIGH)
        GPIO.output(IN2_reerright, GPIO.LOW)
        time.sleep(throttle_reer)

    elif (msg.linear.x < 0.1 and msg.linear.x > -0.1 and msg.angular.z > 0.9 and msg.angular.z < 1.1): # left turn
        rospy.loginfo("left turn")
        GPIO.output(ENB_steering, GPIO.HIGH)
        GPIO.output(IN1_steering, GPIO.HIGH)
        GPIO.output(IN2_steering, GPIO.LOW)
        time.sleep(throttle_steering)


    elif (msg.linear.x > 0.1 and msg.angular.z < 0.0): # right straight
        rospy.loginfo("right straight")
        GPIO.output(ENB_steering, GPIO.HIGH)
        GPIO.output(IN1_steering, GPIO.LOW)
        GPIO.output(IN2_steering, GPIO.HIGH)
        # time.sleep(throxttle_steering)
        
        GPIO.output(ENA_reerleft, GPIO.HIGH)
        GPIO.output(IN1_reerleft, GPIO.HIGH)
        GPIO.output(IN2_reerleft, GPIO.LOW)

        GPIO.output(ENB_reerright, GPIO.HIGH)
        GPIO.output(IN1_reerright, GPIO.HIGH)
        GPIO.output(IN2_reerright, GPIO.LOW)
        time.sleep(throttle_reer)

    elif (msg.linear.x < 0.1 and msg.linear.x > -0.1 and msg.angular.z > -1.1 and msg.angular.z < -0.9): # right turn
        rospy.loginfo("right turn")
        GPIO.output(ENB_steering, GPIO.HIGH)
        GPIO.output(IN1_steering, GPIO.LOW)
        GPIO.output(IN2_steering, GPIO.HIGH)
        time.sleep(throttle_steering)

    if (msg.linear.x < -0.9 and msg.linear.x > -1.1 and msg.angular.z > -0.1 and msg.angular.z < 0.1): # straight
        rospy.loginfo("straight")
        GPIO.output(ENA_reerleft, GPIO.HIGH)
        GPIO.output(IN1_reerleft, GPIO.LOW)
        GPIO.output(IN2_reerleft, GPIO.HIGH)
        GPIO.output(ENB_reerright, GPIO.HIGH)
        GPIO.output(IN1_reerright, GPIO.LOW)
        GPIO.output(IN2_reerright, GPIO.HIGH)
        time.sleep(throttle_reer)
    


def listner():
    rospy.init_node('drive_car', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__=="__main__":
    try: 
        listner()
    except rospy.ROSInterruptException:
        pass
