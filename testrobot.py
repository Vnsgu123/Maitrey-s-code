'''
*****************************************************************************************
*
*        =================================================
*             Pharma Bot Theme (eYRC 2022-23)
*        =================================================
*                                                         
*  This script is intended for implementation of Task 2A   
*  of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  Filename:			task_2a.py
*  Created:				
*  Last Modified:		8/10/2022
*  Author:				e-Yantra Team
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_2a.py
# Functions:		control_logic, detect_distance_sensor_1, detect_distance_sensor_2
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
##############################################################
import  sys
import traceback
import time
import os
import math
from xml.dom.minidom import TypeInfo
from zmqRemoteApi import RemoteAPIClient
import zmq
##############################################################

def control_logic(sim):
    
	"""
	Purpose:
	---
	This function should implement the control logic for the given problem statement
	You are required to actuate the rotary joints of the robot in this function, such that
	it traverses the points in given order

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	None

	Example call:
	---
	control_logic(sim)
	"""
 
	##############  ADD YOUR CODE HERE  ##############
	# sim.simxFinish(-1) # just in case, close all opened connections
	# clientID=simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
	# import sim
	t=1
	l=sim.getObject("/Diff_Drive_Bot")
	# k=sim.getObject("/distance_sensor_1") 
	#j=sim.getObject("/distance_sensor_2")
	h=sim.getObject("/left_joint")
	w=sim.getObject("/right_joint")
	g=sim.getObject("/right_wheel")
	q=sim.getObject("/left_wheel")
	sim.setJointTargetVelocity(h,3)
	sim.setJointTargetVelocity(w,3)

	# distance_2 = detect_distance_sensor_2(sim)
	# distance_1 = detect_distance_sensor_1(sim)
	# print("\nNew")
	# print(distance_2)
	# linearVelocity,angularVelocity=sim.getVelocity(q)
	# print("&&&&&&&&",linearVelocity)
	# sim.setJointTargetVelocity(h,3)
	# sim.setJointTargetVelocity(w,3)
	# linearVelocityy,angularVelocity=sim.getVelocity(g)
	# linearVelocityy2,angularVelocity=sim.getVelocity(q)
	# print("!!!!!!!!!!!!!!!!!!!!!",linearVelocityy,linearVelocityy2)


	pp=0
	v=0
	y=5
	u=1


	while t:
		distance_2 = detect_distance_sensor_2(sim)
		distance_1 = detect_distance_sensor_1(sim)
		if(distance_2<0):
			t=0
		
		# sim.setJointTargetVelocity(h,v)
		if ((float(distance_1)-float(distance_2)) < float(0.03)) and ((float(distance_1)-float(distance_2)) > float(-0.03)):
			print("------")
			# linearVelocity,angularVelocity=sim.getVelocity(q)
			sim.setJointTargetVelocity(h,-3)
			print("++(((((((((((((((((((",distance_2,distance_1)
		if (distance_1 == 0) and ((float(distance_2) > float(0.170)) and (float(distance_2) < float(0.190))):
			# deltaTimeLeft=sim.wait(1,True)
			sim.setJointTargetVelocity(h,3)
			# deltaTimeLeft=sim.wait(1,True)
			print("jnfhuhsy")


			# t=0
	# while y:
	# 	y=y-1
	# while u:

	# 	if((float(distance_2)-float(distance_1)) < float(0.174)):

	# 			linearVelocity,angularVelocity=sim.getVelocity(g)
	# 			linearVelocity2,angularVelocity=sim.getVelocity(q)

	# 			print("&&&&&&&&",linearVelocity,linearVelocity2)
	# 			sim.setJointTargetVelocity(h,2)

      


	# 	print(distance_2)	
		


	#distance2=sim.handleProximitySensor(j)
	# print(distance2)




	# while t:
		# distance_1 = detect_distance_sensor_1(sim)
		# distance_2 = detect_distance_sensor_2(sim)
		# if distance_1==distance_2 and distance_2>0:
		# 	t=0

      
	# detectedObjectHandle=sim.readProximitySensor(j)
	# print(detectedObjectHandle)
	# print(l,k)
	# print(sim)






	##################################################

def detect_distance_sensor_1(sim):
	"""
	Purpose:
	---
	Returns the distance of obstacle detected by proximity sensor named 'distance_sensor_1'

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	distance  :  [ float ]
	    distance of obstacle from sensor

	Example call:
	---
	distance_1 = detect_distance_sensor_1(sim)
	"""
	# distance = None
	# ##############  ADD YOUR CODE HERE  ##############
	k=sim.getObject("/distance_sensor_1")
	# print(k)
	# p,distance1=sim.handleProximitySensor(k)

	# # detectedObjectHandle=sim.readProximitySensor(j)
	# # print(detectedObjectHandle)
	# # distanceData=sim.checkDistance(j,detectedObjectHandle)
	# print(distance1)
	# distance=distance1
	result,distance2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(k)
	print("\nOld-----------")
	print(distance2)
	distance=distance2








	##################################################
	return distance

def detect_distance_sensor_2(sim):
	"""
	Purpose:
	---
	Returns the distance of obstacle detected by proximity sensor named 'distance_sensor_2'

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	distance  :  [ float ]
	    distance of obstacle from sensor

	Example call:
	---
	distance_2 = detect_distance_sensor_2(sim)
	"""
	distance = None
	##############  ADD YOUR CODE HERE  ##############
	j=sim.getObject("/distance_sensor_2")
	# for i in range(1,10):

	# 	pos=sim.getObjectPosition(j,-1)
	# 	pos[2]=i/10
	# 	sim.setObjectPosition(j,-1,pos)
	# 	calculationResults=sim.handleProximitySensor(j)
	# 	print(calculationResults)

	#result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.handleProximitySensor(sim.handle_all_except_explicit)
	#print(distance)



	result,distance2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(j)
	print("\nOld")
	print(distance2)
	distance=distance2

#	result,distance2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.handleProximitySensor(j)

	# detectedObjectHandle=sim.readProximitySensor(j)
	# distanceData=sim.checkDistance(j,detectedObjectHandle)
	
	# distance=calculationResults





	##################################################
	return distance

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THE MAIN CODE BELOW #########

if __name__ == "__main__":
	client = RemoteAPIClient()
	sim = client.getObject('sim')

	try:

		## Start the simulation using ZeroMQ RemoteAPI
		try:
			return_code = sim.startSimulation()
			if sim.getSimulationState() != sim.simulation_stopped:
				print('\nSimulation started correctly in CoppeliaSim.')
			else:
				print('\nSimulation could not be started correctly in CoppeliaSim.')
				sys.exit()

		except Exception:
			print('\n[ERROR] Simulation could not be started !!')
			traceback.print_exc(file=sys.stdout)
			sys.exit()

		## Runs the robot navigation logic written by participants
		try:
			control_logic(sim)
			time.sleep(5)

		except Exception:
			print('\n[ERROR] Your control_logic function throwed an Exception, kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually if required.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

		
		## Stop the simulation using ZeroMQ RemoteAPI
		try:
			return_code = sim.stopSimulation()
			time.sleep(0.5)
			if sim.getSimulationState() == sim.simulation_stopped:
				print('\nSimulation stopped correctly in CoppeliaSim.')
			else:
				print('\nSimulation could not be stopped correctly in CoppeliaSim.')
				sys.exit()

		except Exception:
			print('\n[ERROR] Simulation could not be stopped !!')
			traceback.print_exc(file=sys.stdout)
			sys.exit()

	except KeyboardInterrupt:
		## Stop the simulation using ZeroMQ RemoteAPI
		return_code = sim.stopSimulation()
		time.sleep(0.5)
		if sim.getSimulationState() == sim.simulation_stopped:
			print('\nSimulation interrupted by user in CoppeliaSim.')
		else:
			print('\nSimulation could not be interrupted. Stop the simulation manually .')
			sys.exit()
