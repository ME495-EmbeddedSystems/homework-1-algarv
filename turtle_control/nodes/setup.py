#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill

class Draw:

    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel',Twist,queue_size = 10)
        self.kill = rospy.ServiceProxy("kill", Kill)
        self.spawn = rospy.ServiceProxy("spawn", Spawn)
        self.draw = rospy.Service('draw',Draw,draw())
    
    def draw():
        self.kill("turtle1")
        self.spawn(0,0,0,name="turtle1")


def main():
    rospy.init_node('draw')
    draw = Draw()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass