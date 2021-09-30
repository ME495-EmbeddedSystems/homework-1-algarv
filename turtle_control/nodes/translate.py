import rospy
from geometry_msgs.msg import Twist, Vector3
from turtle_control.msg import TurtleVelocity

def callback(data):
    rospy.loginfo(data)
    pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size = 10)
    twist_value = Twist(Vector3(x=data.x_velocity,y=0,z=0),Vector3(x=0,y=0,z=data.angular_velocity))
    pub.publish(twist_value)

if __name__ == '__main__':
    rospy.init_node('translate')
    rospy.Subscriber('turtle_control/turtle_cmd',TurtleVelocity,callback)
    rospy.spin()