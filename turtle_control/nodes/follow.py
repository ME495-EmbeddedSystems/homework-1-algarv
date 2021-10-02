#!/usr/bin/env python

import rospy
import math
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from turtlesim.msg import Pose 
from turtlesim.srv import Spawn
from std_srvs.srv import Empty
from turtle_control.srv import Start
from turtle_control.msg import TurtleVelocity

dist_thresh = .5 ##this should be a private parameter##

def move_to_waypoint(req): 

    rospy.loginfo(req)

    print("Fuck")

    x = req.x
    y = req.y
    theta = req.theta

    pts = rospy.get_param("/waypoints")
    jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)

    try: 
        target_x = pts[i][0]
        target_y = pts[i][1]
    except:
        i = 0
        target_x = pts[0][0]
        target_y = pts[0][1]

    target_theta = math.atan2((target_y-y),(target_x-x))
    dist = math.sqrt((target_x-x)**2+(target_y-y)**2)
        
    pub = rospy.Publisher('turtle_cmd',TurtleVelocity,queue_size = 10)

    print('Target Theta:', target_theta)
        
    if abs(theta - target_theta)>.1:
        pub.publish(x_velocity = 0, angular_velocity = 1)
    else:
        pub.publish(x_velocity = 0, angular_velocity = 0)
    
    if abs(theta - target_theta)>.1:
        print("Let's go!")
    elif dist > dist_thresh:
        pub.publish(x_velocity = 10, angular_velocity = 0)
    else:
        i = i + 1
        pub.publish(x_velocity = 0, angular_velocity = 0)


def restart(data):

    rospy.loginfo(data)

    start_x = data.start_x
    start_y = data.start_y

    print("Fuck")
    pts = rospy.get_param("/waypoints")
    print(pts)

    total_distance = 0

    for k in range(len(pts)):
        if k == 0:
            dist = math.sqrt((start_x - pts[k][0])**2 + (start_y - pts[k][1])**2)
        else:
            dist = math.sqrt((pts[k][0] - pts[k-1][0])**2 + (pts[k][1] - pts[k-1][1])**2)
        total_distance = total_distance + dist
    
    if start_x < 0 or start_x > 10 or start_y < 0 or start_y > 10: 
        return None
    else:
        rospy.loginfo(total_distance)
        return total_distance
        
    
def main():
    rospy.init_node('follow')

    rospy.wait_for_service('draw')
    draw = rospy.ServiceProxy('draw',Empty)
    draw()


    rospy.Service('restart',Start,restart)

    pub = rospy.Publisher('turtle_cmd',TurtleVelocity,queue_size = 10)
    rospy.Subscriber('/turtle1/pose',Pose,move_to_waypoint)



if __name__ == '__main__':
    main()
    rospy.spin()