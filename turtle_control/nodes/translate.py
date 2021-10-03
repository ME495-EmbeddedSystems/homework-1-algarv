#!/usr/bin/env python

## TRANSLATE NODE ##
'''
The translate node take values published to TurtleVelocity, arranges them into the format expected by the Twist type, and
publishes the final vectors to Twist to change the turtle's velocity.

Subscribers:
    Name: turtle_cmd Type: turtlesim/TurtleVelocity ~ Pulls the linear and angular velocity values from the follow node

Publishers: 
    Name: turtle1/cmd_vel Type: geometry_msgs/Twist ~ Sends re-formatted velocity values to the turtle
'''

import rospy
from geometry_msgs.msg import Twist, Vector3
from turtle_control.msg import TurtleVelocity

#Recieves an argument from the velocity sent from the follow node, and publishes a reorganized value to Twist
def translate(velocity_input):
    rospy.loginfo(velocity_input)
    pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size = 10)
    twist_value = Twist(Vector3(x=velocity_input.x_velocity,y=0,z=0),Vector3(x=0,y=0,z=velocity_input.angular_velocity))
    pub.publish(twist_value)

if __name__ == '__main__':
    rospy.init_node('translate')
    rospy.Subscriber('turtle_cmd',TurtleVelocity,translate)

    rospy.spin()