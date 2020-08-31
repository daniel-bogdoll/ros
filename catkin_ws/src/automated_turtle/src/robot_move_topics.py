import rospy
import random

from geometry_msgs.msg import Twist

#subscriber for the topic that will show location of robot

#publisher for the topic that will make robot move

#what is topic of position --> /pose
#what is topic that makes robot move --> /cmd_vel

def move():
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = random.randint(-10,10)
        twist.angular.z = random.randint(-10,10)

        rospy.loginfo(twist)
        speed_publisher.publish(twist)
        rate.sleep()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel", String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        move()
        listener()
    except rospy.ROSInterruptException:
        pass