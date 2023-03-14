#!/usr/bin/env python3
# A simple ROS subscriber node in Python

import rospy 
from geometry_msgs.msg import Twist

class Subscriber(): 

    def cmd_callback(self, topic_message): 
        print(f"The '{self.node_name}' node obtained the following message: '{str(topic_message)}'")

    def __init__(self): 
        self.node_name = "ez_robot"
        topic_name = "/cmd_vel"

        rospy.init_node(self.node_name, anonymous=True)
        self.sub = rospy.Subscriber(topic_name, Twist, self.cmd_callback)
        rospy.loginfo(f"The '{self.node_name}' node is active...")

    def main_loop(self):
        rospy.spin() 

if __name__ == '__main__': 
    subscriber_instance = Subscriber()
    subscriber_instance.main_loop()
