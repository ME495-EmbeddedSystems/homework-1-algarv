#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from turtlesim.srv import TeleportAbsolute as jump
from std_srvs.srv import Empty

#class Draw:
#
 #   def __init__(self):
 #       self.pub = rospy.Publisher('cmd_vel',Twist,queue_size = 10)
 #       self.draw = rospy.Service('draw',Draw,draw())
 #   def draw(x,y):
 #       jump()


def main():
    pts = rospy.get_param("/waypoints")
    print(pts)
    rospy.init_node('draw')
    reset = rospy.ServiceProxy("reset",Empty)
    spawn = rospy.ServiceProxy("spawn",Spawn)
    for i in range(0,len(pts)):
        jump()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass