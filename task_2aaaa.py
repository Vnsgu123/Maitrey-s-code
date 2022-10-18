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
	j=sim.getObject("/distance_sensor_2")
	h=sim.getObject("/left_wheel_visible")
	g=sim.getObject("/right_wheel_visible")
	# distance_2 = detect_distance_sensor_2(sim)
	distance2=sim.handleProximitySensor(j)
	print(distance2)




	# while t:
		# distance_1 = detect_distance_sensor_1(sim)
		# distance_2 = detect_distance_sensor_2(sim)
		# if distance_1==distance_2 and distance_2>0:
		# 	t=0

      
	# detectedObjectHandle=sim.readProximitySensor(j)
	# print(detectedObjectHandle)
	# print(l,k,j)
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
	# k=sim.getObject("/distance_sensor_1")
	# print(k)
	# p,distance1=sim.handleProximitySensor(k)

	# # detectedObjectHandle=sim.readProximitySensor(j)
	# # print(detectedObjectHandle)
	# # distanceData=sim.checkDistance(j,detectedObjectHandle)
	# print(distance1)
	# distance=distance1







	##################################################
	# return distance

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
	# distance = None
	##############  ADD YOUR CODE HERE  ##############
	# j=sim.getObject("/distance_sensor_2")
	# for i in range(1,10):

	# 	pos=sim.getObjectPosition(j,-1)
	# 	pos[2]=i/10
	# 	sim.setObjectPosition(j,-1,pos)
	# 	calculationResults=sim.handleProximitySensor(j)
	# 	print(calculationResults)


	# result,distance2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.handleProximitySensor(j)

	# detectedObjectHandle=sim.readProximitySensor(j)
	# distanceData=sim.checkDistance(j,detectedObjectHandle)
	# print(distance2)
	# distance=calculationResults





	##################################################
	# return distance

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