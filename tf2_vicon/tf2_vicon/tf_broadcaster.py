import math
import sys

from geometry_msgs.msg import TransformStamped
from interfaces.msg import Position as ViconPose

import numpy as np

import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster

class FramePublisher(Node):
    
    def __init__(self):
        super().__init__('map_baselink_tf_pub')

        self.declare_parameters(namespace='',
                                parameters=[
                                    ('pose_topic', '/vicon_topic'),
                                    ('parent_frame', 'parent_frame'),
                                    ('child_frame', 'child_frame')
                                ])

        self.pose_topic = self.get_parameter('pose_topic').get_parameter_value().string_value
        self.parent_frame = self.get_parameter('parent_frame').get_parameter_value().string_value
        self.child_frame = self.get_parameter('child_frame').get_parameter_value().string_value


        self.tf_broadcaster = TransformBroadcaster(self)

        self.subscription = self.create_subscription(msg_type=ViconPose, 
                                                     topic=self.pose_topic,
                                                     callback=self.handle_vicon_pose,
                                                     qos_profile=1
                                                    )
        
        self.subscription

        self.get_logger().info("Ready to publish vicon tfs")
        self.get_logger().info("Hearing pose from {}".format(self.pose_topic))
        self.get_logger().info("Publishing transform from {} to {}".format(self.parent_frame, self.child_frame))
                            


    def handle_vicon_pose(self, msg: ViconPose):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.parent_frame
        t.child_frame_id = self.child_frame

        t.transform.translation.x = msg.x_trans/1000
        t.transform.translation.y = msg.y_trans/1000
        t.transform.translation.z = 0.0

        t.transform.rotation.x = msg.x_rot
        t.transform.rotation.y = msg.y_rot
        t.transform.rotation.z = msg.z_rot
        t.transform.rotation.w = msg.w

        self.tf_broadcaster.sendTransform(t)


def main():
    rclpy.init()
    node = FramePublisher()
    try:
        rclpy.spin(node)
    except:
        pass
        
    
    rclpy.shutdown()








