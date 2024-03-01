#!/usr/bin/env python
import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

goal = MoveBaseGoal()
xx = input("Enter your value x: ")
yy = input("Enter your value y: ")
zz = input("Enter your value z: ")
ww = input("Enter your value w: ")
client.send_goal(goal)
client.wait_for_result()

goal.target_pose.header.frame_id = 'odom' 
goal.target_pose.pose.position.x = xx
goal.target_pose.pose.position.y = yy
goal.target_pose.pose.orientation.z = zz
goal.target_pose.pose.orientation.w = ww

client.send_goal(goal)
client.wait_for_result()
