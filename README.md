# WiiRobotArm
Wii Remote control robot arm with the Raspberry Pi

  This program is written in python using the python CWiiD library.
Using Cwiid its able to connect to the WiiRemote via Bluetooth and allows python to interpret the data from the accelerameter
to get the data for the tilt and roll, as well as button presses. The program then uses that data to control some L298N H-bridges
wired to the GPIO pins on the RaspberryPi, to control the speed and direction of the DC Motors. In the case of my project the DC motors are connected to my Elenco OWI535
robotic Arm. 

  The Roll of the remote controls the left or right, and the tilt controlls the arm's up and down movement. The steeper the angle
the quicker the arm moves in the given direction. The Up and Down on the D-Pad controls the tilt of the claw. 
The A Button opens the claw and the B Button closes the claw. 
