#!/usr/bin/env python
import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

goal = MoveBaseGoal()
client.send_goal(goal)
client.wait_for_result()

goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = 0.5
goal.target_pose.pose.position.y = 0.5
goal.target_pose.pose.orientation.z = 0.0
goal.target_pose.pose.orientation.w = 1

client.send_goal(goal)
client.wait_for_result()
