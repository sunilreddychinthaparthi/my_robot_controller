#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        #create a publisher to send movement commands to the turtle
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        #create a subscriber to listen to the live co ordinates of the turtle
        #notice that its callback is self.pose_callback, which means that every time a new pose message is received, the pose_callback function will be called
        self.pose_subscriber = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.get_logger().info('Turtle Controller Node has been started.')

    def pose_callback(self, pose: Pose):
        #balnk movement message
        cmd= Twist()

        #closed loop logic to check boundaries(screen limits are roughly 0.0 to11.0)
        if pose.x>10.0 or pose.x<2.0 or pose.y>10.0 or pose.y<2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 1.0
        else:
            cmd.linear.x = 3.0
            cmd.angular.z = 0.0

            #instantly send out the calculated movement command to the turtle
        self.cmd_vel_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)

    node = TurtleControllerNode()

    rclpy.spin(node)

    rclpy.shutdown()

    if __name__ == '__main__':
        main()