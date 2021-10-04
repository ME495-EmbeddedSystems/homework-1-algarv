#!/usr/bin/env python

## FOLLOW NODE ##
'''
The follow node calls the draw service to set-up the waypoints for the turtle, then waits for the restart paramter to be called to set the turtle
at the given starting coordinates and finally directing it to each waypoint. 

Service Calls:
    Name: /draw Type: /std_srvs.srv/Empty ~ Sends the turtle to each waypoint and draws an X

    Name: /turtle1/teleport_absolute Type: turtlesim/TeleportAbsolute ~ Make the turtle jump to a new position 

    Name: /turtle1/set_pen Type: turtlesim/SetPen ~ Toggles the pen function and sets color and width

Custom Services:
    Name: /restart Type: turtle_control/Start ~ Moves the turtle to the given starting coordinates and calculates the total travel distance 

Subscribers:
    Name: /pose Type: turtlesim/Pose ~ Returns the current turtle position

Publishers:
    Name: turtle_cmd Type: turtlesim/TurtleVelocity ~ Gives the turtle a linear and angular velocity

Parameters: 
    Name: /waypoints ~ Waypoint coordinates

    Name: /dist_thresh ~ Distance threshold value
'''


from os import setgroups
import rospy
import math
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose 
from turtlesim.srv import SetPen
from std_srvs.srv import Empty
from turtle_control.srv import Start
from turtle_control.msg import TurtleVelocity

def move_to_waypoint(Pose): 
    '''
    Called from the restart function.
    Takes argument from Pose topic, and extracts the x, y, and theta positions which will constantly update. 
    Uses waypoints parameters as the target coordinates and calculates the distance away using the Pose values.
    Determines the necessary motions and publishes a cooresponding velocity to TurtleVelocity.
    '''
    rospy.loginfo(Pose)
    global i
    global run_count

    x = Pose.x
    y = Pose.y
    theta = Pose.theta
    pts = rospy.get_param("/waypoints")

    dist_thresh = rospy.get_param("/dist_thresh")

    target_x = pts[i][0]
    target_y = pts[i][1]

    target_theta = math.atan2((target_y-y),(target_x-x))
    dist = math.sqrt((target_x-x)**2+(target_y-y)**2)

    pub = rospy.Publisher('turtle_cmd',TurtleVelocity,queue_size = 10)

    print("Target X:", target_x)
    print("Target_Y", target_y)
    print("Target Theta: ", target_theta)
    print("Target Dist: ", dist)

    print("Theta: ", theta)
    print("Dist: ", dist)
    

    if dist > dist_thresh:
        if abs(theta - target_theta)>.1:
            pub.publish(x_velocity = 0, angular_velocity = 3)
        else:
            pub.publish(x_velocity = 5, angular_velocity = 0)
    else:
        if i >= len(pts)-1:
            i = 0
            run_count = run_count + 1
        else:
            i = i + 1
        print("Counter: ", i)



def restart(start_input):
    '''
    Takes argument from the input from the start service call for the starting coordinate of the turtle. 
    Sends the turtle to the inputed start coordinates, sets the pen to draw, and calculates then returns the total distance to travel 
        from the starting point to each of the waypoints (pulled from the waypoints parameter). 
    '''
    rospy.loginfo(start_input)
    jump = rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
    setpen = rospy.ServiceProxy("/turtle1/set_pen",SetPen)

    start_x = start_input.start_x
    start_y = start_input.start_y

    jump(start_x,start_y,0)
    setpen(0,255,0,2,0)

    global i
    global run_count
    i = 0
    run_count = 1
    rospy.Subscriber('/turtle1/pose',Pose,move_to_waypoint)
    
    pts = rospy.get_param("/waypoints")

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



if __name__ == '__main__':
    main()
    rospy.spin()