#Ultrasonic Sensor Program
#TO measure the distance to an obstacle
#Author:Khadija AMH (VIMAN's Group) Date: 24/07/2018


import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.IN)

while True:
         GPIO.output(16,True)       #20 Pin connected to Trigger//Transmits a signal
         time.sleep(0.05)
         GPIO.output(16,False)      #Stops the transmitting
         
         while(GPIO.input(21)==0):  #21 Pin connected to Echo
                t=time.time()       #Transmitting Time
         while(GPIO.input(21)==1):
                r=time.time()       #Reception time
         timep=(r-t)/2	            
         dis = timep *36400	    #Half-Distance travelled by wave

         print 'Distance to obstacle is %d cm' %dis
