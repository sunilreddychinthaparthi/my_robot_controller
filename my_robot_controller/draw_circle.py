#!/usr/bin`/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.1, self.send_velocity_command)
        self.get_logger().info('Drawing a circle...')

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 5.0
        msg.angular.z = 2.5
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = DrawCircleNode()

    rclpy.spin(node)

    rclpy.shutdown()