#!/usr/bin/env python

import rospy
import math
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose

def main():
    rospy.init_node('follow')
    pts = rospy.get_param("/waypoints")
    jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
    pose = rospy.get_param("/turtle1/Pose", Pose)
    for j in range(len(pts)):
        x = pts[j][0]
        y = pts[j][1]
        target_x = pose.x
        target_y = pose.y
        dist = math.sqrt((target_x-x)**2+(target_y-y)**2)
        while dist > .5:
            jump(x-.1,y-.1,0)

    
         
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass