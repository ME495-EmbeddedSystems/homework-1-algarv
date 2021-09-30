import rospy

def main():
    rospy.init_node('follow')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass