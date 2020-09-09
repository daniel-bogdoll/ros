#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
ros::Publisher velocity_publisher;

void move (double speed, double distance, bool isForward) {
    //Topic turtle1/cmd_vel is responsible for moving
    //Message type is geometry_msgs/wist
    geometry_msgs::Twist vel_msg;

    if (isForward)
        vel_msg.linear.x = abs(speed);
    else
        vel_msg.linear.x = -abs(speed);
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;
    vel_msg.angular.z = 0;

    double tStart = ros::Time::now().toSec();
    double currentDistance = 0;
    ros::Rate loopRate(10);
    do{
        velocity_publisher.publish(vel_msg);
        double tNow = ros::Time::now().toSec();
        currentDistance = speed * (tNow - tStart);
        ros::spinOnce();
        loopRate.sleep();
    }while(currentDistance < distance);
    vel_msg.linear.x = 0;
    velocity_publisher.publish(vel_msg);
    ros::spinOnce(); //necessary?
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_cleaner");
    ros::NodeHandle n;

    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

    move (2.0, 5.0, 1);
}