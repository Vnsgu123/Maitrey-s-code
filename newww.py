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
from difflib import diff_bytes
import  sys
import traceback
import time
import os
import math
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

	# q=objectHandle=sim.getObject("/distance_sensor_1")
	# w=objectHandle=sim.getObject("/distance_sensor_2")
	e=objectHandle=sim.getObject("/left_joint")
	r=objectHandle=sim.getObject("/right_joint")
	t=objectHandle=sim.getObject("/right_wheel")
	y=objectHandle=sim.getObject("/left_joint")
	# list=[]
	# list.append(0)
	# list.append(0)
	# list.append(0)
	list=[]
	list.append(30.0)
	# list1.append(0)
	# list1.append(0)
	# sim.setJointTargetForce(e,0)
	# sim.setJointTargetForce(r,0)
	# sim.addForceAndTorque(y,list,list1)
	# sim.addForceAndTorque(t,list,list1)
	# linearVelocity,angularVelocity=sim.getObjectVelocity(e)
	# linearVelocity1,angularVelocity=sim.getObjectVelocity(r)


	# sim.setJointTargetVelocity(e,4)
	# sim.setJointTargetVelocity(r,4)
	oo=sim.getJointTargetVelocity(y)
	print(oo)

	bb=1
	while bb:
		t=1
		m=1
		n=1
		p=1
		while t:
			distance_1 = detect_distance_sensor_1(sim)
			distance_2 = detect_distance_sensor_2(sim)
			print(distance_1)
			print(distance_2)
			diff=distance_1 - distance_2
			print("--------",diff)
			if diff < 0.065 and diff > -0.065:
				print("iiiiii")
				t=0
				# yy=1s
				sim.setJointTargetVelocity(e,-oo)
				# sim.setJointTargetVelocity(r,)
		while m:	
			distance_11 = detect_distance_sensor_1(sim)
			distance_22 = detect_distance_sensor_2(sim)
			print(distance_22,distance_11)
			if (distance_11==0) and (distance_22 >= 0.166 and distance_22 <= 0.182):
				print("@@@@@@@")
				# sim.Simulation()
				# resultt=sim.pauseSimulation()
				# sim.setJointTargetVelocity(e,-2)
				# sim.setJointTargetVelocity(e,-3)
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(e,2)
				# sim.setJointTargetVelocity(e,3)
				# time.sleep(0.5)
				sim.setJointTargetVelocity(e,oo)	
				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m=0
		while n:
			# sim.setJointTargetVelocity(e,4,2)
			# sim.setJointTargetVelocity(r,4)
			n=0
		# while p:
		# 	print()

     




	# print(distance_1)
	# print(distance_2)


	# print(q)





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
	distance = None
	##############  ADD YOUR CODE HERE  ##############

	q=objectHandle=sim.getObject("/distance_sensor_1")
	result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(q)




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

	w=objectHandle=sim.getObject("/distance_sensor_2")
	result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(w)



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
