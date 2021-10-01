#!/usr/bin/env python

import rospy
import math
#from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from std_srvs.srv import Empty


dist_thresh = .5 ##this should be a private parameter##

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

def restart(start_x, start_y):
    spawn = rospy.ServiceProxy("turtle1/spawn",Spawn)
    spawn(start_x,start_y,0)

    pts = rospy.get_param("/waypoints")

    total_distance = 0

    for k in range(len(pts)):
        if k = 0:
            dist = math.sqrt((start_x - pts[k][0])**2 + (start_y - pts[k][1])**2)
        else:
            dist = math.sqrt((pts[k][0] - pts[k-1][0])**2 + (pts[k][1] - pts[k-1][1])**2)
        total_distance = total_distance + dist
    
    if start_x < 0 or start_x > 10 or start_y < 0 or start_y > 10: 
        return None
    else:
        return total_distance
    
def main():
    rospy.init_node('follow')
    rospy.wait_for_service('draw')
    draw = rospy.ServiceProxy('draw',Empty)
    draw()

    rospy.Service('restart','turtle_control/Start',restart)

    rospy.Subscriber('/turtle1/Pose',Pose,callback)

if __name__ == '__main__':
    main()
    rospy.spin()