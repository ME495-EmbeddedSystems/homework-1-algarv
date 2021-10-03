#!/usr/bin/env python

## SET-UP NODE ##
'''
The set-up node creates the draw service, which pulls the waypoint coordinates from the waypoints parameter and utilizes the 
TeleportAbsolute and SetPen services to mark each waypoint with an X. The draw service is called by the follow node to set-up 
the board.

Service Calls:

    Name: /turtle1/teleport_absolute Type: turtlesim/TeleportAbsolute ~ Make the turtle jump to a new position 

    Name: /turtle1/set_pen Type: turtlesim/SetPen ~ Toggles the pen function and sets color and width

Custom Services: 

    Name: /draw Type: /std_srvs.srv/Empty ~ Sends the turtle to each waypoint and draws an X

Parameters: 

    Name: /waypoints ~ Waypoint coordinates
'''
import rospy
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import SetPen
from std_srvs.srv import Empty, EmptyResponse


#Draw_waypoints takes no arguments but uses the waypoints parameters to send the turtle to each set of coordinates
#and draws 4 line segments from the center to make an X
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

    return EmptyResponse() #No return values are needed, the purpose of this function is just to draw the Xs at each waypoint

def main():
    rospy.init_node('draw')
    s = rospy.Service('draw',Empty,draw_waypoints)


if __name__ == '__main__':
    main()
    rospy.spin()