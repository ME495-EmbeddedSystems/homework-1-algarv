#!/usr/bin/env python

import rospy
import math
#from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from turtlesim.msg import Pose
from std_srvs.srv import Empty

#from Start.srv import Start

dist_thresh = .5

def callback(data):
    rospy.loginfo(data)
    x = Pose.x
    y = Pose.y
    pts = rospy.get_param("/waypoints")
    move = rospy.ServiceProxy("/turtle1/teleport_relative",TeleportRelative)
    #restart = rospy.ServiceProxy("/turtle_control/Start",Start)
    #jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)

    for j in range(len(pts)):
        target_x = pts[j][0]
        target_y = pts[j][1]
        dist = math.sqrt((target_x-x)**2+(target_y-y)**2)
        theta = math.atan2((target_y-y)/(target_x-x))
        move(dist,theta)

def main():
    rospy.init_node('follow')
    rospy.wait_for_service('draw')
    draw = rospy.ServiceProxy('draw',Empty)
    draw()

    rospy.Subscriber('/turtle1/Pose',Pose,callback)

if __name__ == '__main__':
    main()
    rospy.spin()