'''
*****************************************************************************************
*
*        =================================================
*             Pharma Bot Theme (eYRC 2022-23)
*        =================================================
*                                                         
*  This script is intended for implementation of Task 2B   
*  of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  Filename:			task_2b.py
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
# Filename:			task_2b.py
# Functions:		control_logic, read_qr_code
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
import numpy as np
import cv2
import random
from pyzbar.pyzbar import decode
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def control_logic(sim):
	"""
	Purpose:
	---
	This function should implement the control logic for the given problem statement
	You are required to make the robot follow the line to cover all the checkpoints
	and deliver packages at the correct locations.

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
	defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
	sim.setInt32Param(sim.intparam_idle_fps, 0)

	e=sim.getObject("/left_joint")
	r=sim.getObject("/right_joint")
	m=sim.getObject("/vision_sensor")

	sim.setJointTargetVelocity(e,1)
	sim.setJointTargetVelocity(r,1)
	t=1
	i=1
	flag4=0
	flag=0
	flag1=0
	flag2=1
	flag6=0
	while t:
		u=0
		print("run")
		img, resX, resY = sim.getVisionSensorCharImage(m)
		# print(type(resX))
		# resX=resX-20
		# print(resX)
		img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
		img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
		# print(img.shape)
		img=img[0:512,70:442]
		hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		low_b = np.array([0,0,168])
		high_b = np.array([172,111,255])
		yellow_lower = np.array([20, 100, 100])
		yellow_upper = np.array([30, 255, 255])
		mask = cv2.inRange(hsv, low_b, high_b)
		mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
		out = cv2.bitwise_and(img,img, mask= mask)
		out1 = cv2.bitwise_and(img,img, mask= mask1)
		contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
		contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)
		for contour in contours:
			approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
			x,y,w,h=cv2.boundingRect(contour)
			cv2.drawContours(img, [approx], 0, (0, 255, 255), 5)

			print(x,y,w,h,len(contour))

			# print("%%%%%%",w)
			if ((w < 34  and w>20) or (w > 39 and w < 43)) and len(contour) < 374 and len(contour)>200:
				# if w < 60 and w > 20 and len(contour) < 375 and len(contour) > 200:
				u=u+1
				cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
				ll=len(contour)
				print("----------",ll,w)
				M = cv2.moments(contour)
				if M["m00"] !=0 :
					cx = int(M['m10']/M['m00'])
					cy = int(M['m01']/M['m00'])
					print("CX : "+str(cx)+"  CY : "+str(cy))
				# if cy < 100 and flag6 ==1 :
				# 	sim.setJointTargetVelocity(e,1)
				# 	flag6=0
				if cx < 179 :
					print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
					sim.setJointTargetVelocity(e,0.7)
					sim.setJointTargetVelocity(r,1.3)
     
				elif cx > 183 :
					print("####################################################")
					sim.setJointTargetVelocity(r,0.9)
					sim.setJointTargetVelocity(e,1.1)

				else :
					# if flag6 ==0:
					sim.setJointTargetVelocity(e,1)
					sim.setJointTargetVelocity(r,1)
		q=0
		flag3=0
		for contour in contours1:
			flag3=1
			flag4=1
			print(len(contour))
			q=q+1
			approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
			# if len(contour) >2000:
			# 	flag=1
			cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
		if q==13 and flag2==1:
			sim.setJointTargetVelocity(e,0)
			sim.setJointTargetVelocity(r,0)
			print("maiyfesysifdisfsfisffi")
			flag1=1
			flag2=0
			# activate_qr_code()
			# read_qr_code(sim)s
			# deactivate_qr_code()

			sim.setJointTargetVelocity(e,1)
			sim.setJointTargetVelocity(r,1)
		print(flag1,cx,cy)
		if flag1==1 and cx >150 and cy > 0 and cy < 100 and flag3==0 :
			if i==1:
				turnleft()
			if i==2:
				turnright()
			if i==3:
				turnleft()
			if i==4:
				turnright()
			if i==6:
				turnright()
			if i==7:
				turnleft()
			if i==8:
				turnright()
			if i==10:
				turnright()
       
			# sim.setJointTargetVelocity(e,1)
			# sim.setJointTargetVelocity(r,1)

			# if flag4==1 and flag3==0:
			# sim.setJointTargetVelocity(e,-1)
			flag1=0
			flag2=1
			i=i+1
				
			print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
			# y=1
			# while y:
			# 	flag4=0
			# 	# print("runkkk")
			# sim.setJointTargetVelocity(r,1)

	




		# if u>=7 and cy > 440 and cy <450 :
		# 	flag=flag+1
		# if cy > 440 and cy < 450 and u>=7 and flag==1:
		# 	sim.setJointTargetVelocity(e,0)
		# 	sim.setJointTargetVelocity(r,0)
		# 	print("maitrey")
		# 	# activate_qr_code()
		# 	# read_qr_code(sim)s
		# 	# deactivate_qr_code()
		# 	sim.setJointTargetVelocity(e,1)
		# 	sim.setJointTargetVelocity(r,1)
		# if cy > 400 and u==7 and flag==2:
		# 	print("patel")
		# 	sim.setJointTargetVelocity(e,-1)




		cv2.imshow('maitrey',img)
		cv2.imshow('mask',mask)
		cv2.imshow('mask1',mask1)
		# cv2.imshow('out',out)
		cv2.waitKey(1)
		client.step()  # triggers next simulation step



	##################################################

def read_qr_code(sim):
	"""
	Purpose:
	---
	This function detects the QR code present in the camera's field of view and
	returns the message encoded into it.

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	`qr_message`   :    [ string ]
		QR message retrieved from reading QR code

	Example call:
	---
	control_logic(sim)
	"""
	qr_message = None
	##############  ADD YOUR CODE HERE  ##############

	##################################################
	return qr_message

def turnleft():
    
	e=sim.getObject("/left_joint")
	r=sim.getObject("/right_joint")
	sim.setJointTargetVelocity(r,1)
	sim.setJointTargetVelocity(e,-1)
	m=sim.getObject("/vision_sensor")
	time.sleep(1.5)

	t=1
	while t:
		u=0
		print("run")
		img, resX, resY = sim.getVisionSensorCharImage(m)
		# print(type(resX))
		# resX=resX-20
		# print(resX)
		img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
		img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
		print(img.shape)
		img=img[0:512,70:442]
		hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		low_b = np.array([0,0,168])
		high_b = np.array([172,111,255])
		# yellow_lower = np.array([20, 100, 100])
		# yellow_upper = np.array([30, 255, 255])
		mask = cv2.inRange(hsv, low_b, high_b)
		# mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
		out = cv2.bitwise_and(img,img, mask= mask)
		# out1 = cv2.bitwise_and(img,img, mask= mask1)
		contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
		# contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)32,128
		for contour in contours:
			approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
			x,y,w,h=cv2.boundingRect(contour)
			cv2.drawContours(img, [approx], 0, (0, 255, 255), 5)

			# print(x,y,w,h)

			# print("%%%%%%",w)
			if w < 34  and w>26 and len(contour) < 350 and len(contour)>290 :
				u=u+1
				cv2.drawContours(img, [approx], 0, (255, 0, 255), 5)
				ll=len(contour)
				print("----------",ll,w)
				M = cv2.moments(contour)
				if M["m00"] !=0 :
					cx = int(M['m10']/M['m00'])
					cy = int(M['m01']/M['m00'])
					print("CX : "+str(cx)+"  CY : "+str(cy))
					time.sleep(0.3)
					t=0

		# print("run")
		# img, resX, resY = sim.getVisionSensorCharImage(m)
		# img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
		# img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
		# hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		# low_b = np.array([0,0,168])
		# high_b = np.array([172,111,255])
		# # yellow_lower = np.array([20, 100, 100])
		# # yellow_upper = np.array([30, 255, 255])
		# mask = cv2.inRange(hsv, low_b, high_b)
		# # mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
		# out = cv2.bitwise_and(img,img, mask= mask)
		# # out1 = cv2.bitwise_and(img,img, mask= mask1)
		# contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
		# for contour in contours:
		# 	approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
		# 	x,y,w,h=cv2.boundingRect(contour)
		# 	# print(x,y,w,h)
   
		# 	# print("%%%%%%",w)
		# 	if w < 34 and w>27 and len(contour) < 350 and len(contour)>280:
		# 		u=u+1
		# 		cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
		# 		ll=len(contour)
		# 		print("----------",ll,w)
		# 		M = cv2.moments(contour)
		# 		if M["m00"] !=0 :
		# 			cx = int(M['m10']/M['m00'])
		# 			cy = int(M['m01']/M['m00'])
		# 			print("CX : "+str(cx)+"  CY : "+str(cy))
		# 			# if cx <215 and cx > 200 and cy < 70:
		# 			sim.setJointTargetVelocity(e,-1)
		# 			t=0
		cv2.imshow('maitrey',img)
		cv2.waitKey(1)
		client.step()  # triggers next simulation step
	return

def turnright():
    
	e=sim.getObject("/left_joint")
	r=sim.getObject("/right_joint")
	sim.setJointTargetVelocity(e,1)
	sim.setJointTargetVelocity(r,-1)
	m=sim.getObject("/vision_sensor")
	time.sleep(1.5)

	t=1
	while t:
		u=0
		print("run")
		img, resX, resY = sim.getVisionSensorCharImage(m)
		# print(type(resX))
		# resX=resX-20
		# print(resX)
		img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
		img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
		print(img.shape)
		img=img[0:512,70:442]
		hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		low_b = np.array([0,0,168])
		high_b = np.array([172,111,255])
		# yellow_lower = np.array([20, 100, 100])
		# yellow_upper = np.array([30, 255, 255])
		mask = cv2.inRange(hsv, low_b, high_b)
		# mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
		out = cv2.bitwise_and(img,img, mask= mask)
		# out1 = cv2.bitwise_and(img,img, mask= mask1)
		contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
		# contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)
		for contour in contours:
			approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
			x,y,w,h=cv2.boundingRect(contour)
			cv2.drawContours(img, [approx], 0, (0, 255, 255), 5)

			# print(x,y,w,h)

			# print("%%%%%%",w)
			if w < 34  and w>26 and len(contour) < 350 and len(contour)>270 :
				u=u+1
				cv2.drawContours(img, [approx], 0, (255, 0, 255), 5)
				ll=len(contour)
				print("----------",ll,w)
				M = cv2.moments(contour)
				if M["m00"] !=0 :
					cx = int(M['m10']/M['m00'])
					cy = int(M['m01']/M['m00'])
					print("CX : "+str(cx)+"  CY : "+str(cy))
					time.sleep(0.3)
					t=0

		# print("run")
		# img, resX, resY = sim.getVisionSensorCharImage(m)
		# img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
		# img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
		# hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		# low_b = np.array([0,0,168])
		# high_b = np.array([172,111,255])
		# # yellow_lower = np.array([20, 100, 100])
		# # yellow_upper = np.array([30, 255, 255])
		# mask = cv2.inRange(hsv, low_b, high_b)
		# # mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
		# out = cv2.bitwise_and(img,img, mask= mask)
		# # out1 = cv2.bitwise_and(img,img, mask= mask1)
		# contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
		# for contour in contours:
		# 	approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
		# 	x,y,w,h=cv2.boundingRect(contour)
		# 	# print(x,y,w,h)
   
		# 	# print("%%%%%%",w)
		# 	if w < 34 and w>27 and len(contour) < 350 and len(contour)>280:
		# 		u=u+1
		# 		cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
		# 		ll=len(contour)
		# 		print("----------",ll,w)
		# 		M = cv2.moments(contour)
		# 		if M["m00"] !=0 :
		# 			cx = int(M['m10']/M['m00'])
		# 			cy = int(M['m01']/M['m00'])
		# 			print("CX : "+str(cx)+"  CY : "+str(cy))
		# 			# if cx <215 and cx > 200 and cy < 70:
		# 			sim.setJointTargetVelocity(e,-1)
		# 			t=0
		cv2.imshow('maitrey',img)
		cv2.waitKey(1)
		client.step()  # triggers next simulation step
	return






    


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
			time.sleep(5)
			control_logic(sim)

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