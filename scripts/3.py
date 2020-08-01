#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
import time
PI = 3.1415926535897
def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
  
    while not rospy.is_shutdown():
        time.sleep(1)
        speed = 2
        distance = input("Type your distance:")
        #isForward = input("Foward?: ")#True or False 

        vel_msg.linear.x = speed
    	vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0 
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        while(current_distance < distance):
	    velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        time.sleep(1)

        speed = 100
        angle = input("Type your distance (degrees):")
        #isForward = input("Clockwise?: ")

        angular_speed = speed*2*PI/360
        relative_angle = angle*2*PI/360


        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.y = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angular_speed
        t0 = rospy.Time.now().to_sec()
        
    	
        current_angle = 0
        while(current_angle < relative_angle):
	    velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
