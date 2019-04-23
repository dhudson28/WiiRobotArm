#!/usr/bin/env python

import cwiid, time
import pdb
import RPi.GPIO as gpio

button_delay = 0.1
ac = 0 #set flag for accelerometer
print("please press buttons 1 + 2 on wiimote")

time.sleep(1)
state = 0
try:
	wii=cwiid.Wiimote()
	#pdb.set_trace()
	wii.rpt_mode = cwiid.RPT_ACC | cwiid.RPT_BTN
	
except:
	print("try again")
	quit()
pdb.set_trace() #Enables the debugger
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT) #goes to ENB pin
gpio.setup(11, gpio.OUT) #goes to ENA pin

#These are for A_Motor
gpio.setup(13, gpio.OUT) #this goes to IN1 pin
gpio.setup(15, gpio.OUT) #this goes to IN2 pin
#These are for B_Motor
gpio.setup(35, gpio.OUT)
gpio.setup(37, gpio.OUT)
#These are for the claw
gpio.setup(36, gpio.OUT)
gpio.setup(38, gpio.OUT)
#These are for the claw tilt
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
#These enable speed
motorSpeed_Roll = gpio.PWM(7, 100) #engage ENB
motorSpeed_Tilt = gpio.PWM(11, 100) #engage ENA
motorSpeed_Roll.start(0)
motorSpeed_Tilt.start(0)
	#time.sleep(0.1)
	

while True:
	roll = wii.state['acc'][0]
	tilt = wii.state['acc'][1]
	speed_tilt = abs(wii.state['acc'][1] - 128) * 2
	speed_roll = abs(wii.state['acc'][0] - 128) * 2
	buttonValue = wii.state['buttons']
	
	#print(roll)
	#pdb.set_trace()	
	try:	#this code below is for the arm up and down based on the tild of the remote
		if(tilt > 135):#This will make the motor go forwards
			gpio.output(13, True)#when the controller is up
			gpio.output(15, False)
			motorSpeed_Tilt.ChangeDutyCycle(speed_tilt)
		if(tilt < 120):
			gpio.output(13, False)
			gpio.output(15, True)
			motorSpeed_Tilt.ChangeDutyCycle(speed_tilt)
		if(tilt < 135 and tilt > 120):
			gpio.output(13, False)
			gpio.output(15, False)
			
		#this code below is for the arm left to right movement
		if(roll > 125):
			gpio.output(35, True)
			gpio.output(37, False)
			motorSpeed_Roll.ChangeDutyCycle(speed_roll)
		if(roll < 123):
			gpio.output(35, False)
			gpio.output(37, True)
			motorSpeed_Roll.ChangeDutyCycle(speed_roll)
		if(roll < 125 and roll > 123):
			gpio.output(35, False)
			gpio.output(37, False)
			
		#This code is for the claw, to open(A button) or close(B button)
		if(buttonValue == 4):
			gpio.output(36, True)
			gpio.output(38, False)
		if(buttonValue == 8):
			gpio.output(36, False)
			gpio.output(38, True)
		if(buttonValue == 0):
			gpio.output(16, False)
			gpio.output(18, False)
			gpio.output(36, False)
			gpio.output(38, False)	
		#adding code for the claw tilt
		if(buttonValue == 2048):
			gpio.output(16, False)
			gpio.output(18, True)
		if(buttonValue == 1024):
			gpio.output(16, True)
			gpio.output(18, False)
	except:
		continue
if KeyboardInterrupt:
	gpio.cleanup()
		
	
