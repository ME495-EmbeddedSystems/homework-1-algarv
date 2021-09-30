#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from turtlesim.srv import SetPen
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
    #reset = rospy.ServiceProxy("reset",Empty)
    spawn = rospy.ServiceProxy("/spawn",Spawn)
    jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
    setpen = rospy.ServiceProxy("/turtle1/set_pen",SetPen)
    #spawn(0,0,0,"Turtle")
    for i in range(0,len(pts)):
        x = pts[i][0]
        y = pts[i][1]
        setpen(255,0,0,2,1)
        jump(x,y,0)
        setpen(255,0,0,2,0)
        jump(x+.5,y+.5,0)
        setpen(255,0,0,2,1)
        jump(x,y,0)
        setpen(255,0,0,2,0)
        jump(x-.5,y-.5,0)
        setpen(255,0,0,2,1)
        jump(x,y,0)
        setpen(255,0,0,2,0)
        jump(x-.5,y+.5,0)
        setpen(255,0,0,2,1)
        jump(x,y,0)
        setpen(255,0,0,2,0)
        jump(x+.5,y-.5,0)
        setpen(255,0,0,2,1)
    
    jump(5.5,5.5,0)
    


    #rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass