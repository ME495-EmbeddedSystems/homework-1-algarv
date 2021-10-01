#!/usr/bin/env python

import rospy
import math
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
from Start.srv import Start

dist_thresh = .5

def callback(data):
    rospy.loginfo(data)
    x = Pose.x
    y = Pose.y
    pts = rospy.get_param("/waypoints")
    start = rospy.ServiceProxy("/turtle_control/Start",Start)
    jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
    for j in range(len(pts)):
        jump(0,0,0)
        target_x = pts[j][0]
        target_y = pts[j][1]
        dist = math.sqrt((target_x-x)**2+(target_y-y)**2)
        while dist > dist_thresh:
            jump(x-.1,y-.1,0)

if __name__ == '__main__':
    rospy.init_node('follow')
    rospy.Subscriber('/turtle1/Pose',Pose,callback)
    rospy.spin()