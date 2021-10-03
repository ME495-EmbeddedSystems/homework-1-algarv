#!/usr/bin/env python

import rospy
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from turtlesim.srv import SetPen
from turtlesim.msg import Pose
from std_srvs.srv import Empty, EmptyResponse

def draw_waypoints(req):
    pts = rospy.get_param("/waypoints")
    jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
    setpen = rospy.ServiceProxy("/turtle1/set_pen",SetPen)
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

    return EmptyResponse()

def main():
    rospy.init_node('draw')
    s = rospy.Service('draw',Empty,draw_waypoints)


if __name__ == '__main__':
    main()
    rospy.spin()