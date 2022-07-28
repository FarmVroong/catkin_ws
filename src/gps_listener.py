#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
import time
from sensor_msgs.msg import NavSatFix

def callback(msg):
    rospy.loginfo("latitude: [%f]"%(msg.latitude))


def gps_listner():
    rospy.init_node('gps_listener', anonymous=True)
    rospy.Subscriber("fix", NavSatFix,callback)
    rospy.spin()

if __name__=="__main__":
    try: 
        gps_listner()
        rospy.loginfo("gps node started")
    except rospy.ROSInterruptException:
        pass