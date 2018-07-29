#IR Sensor program: To sense an interruption
#LED blinks when there is an interruption
#Message Box appears when there is an Interruption
#Author: Khadija AMH (VIMAN's Group) Date: 24/07/2018


import time
import Tkinter
import tkMessageBox
import RPi.GPIO as GPIO

#setting up the GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)  #Setting the IR Sensor to INPUT
GPIO.setup(20,GPIO.OUT) #Setting the LED to Output

#To count number of interruptions that occur
count=0
while True:
	a=GPIO.input(21)
	if(not a):
                GPIO.output(20,True)            #LED Switches on when there is Interruption
                #Message Box
		tkMessageBox.showwarning('Interrupted','Signal has been interrupted %d' %count)
		count=count+1
	else:
		GPIO.output(20,False)
 
	
