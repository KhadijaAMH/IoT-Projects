#Motor Program: TO make the motor (2 Wheels) move forward,back,left and right and stop
#Author:Khadija AMH (VIMAN's Group) Date: 25/07/2018

import RPi.GPIO as GPIO
import time

#To set the modes

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

#Forward
def forward():
    #Left Wheel
    GPIO.output(12,False)
    GPIO.output(16,True)
    #Right Wheel
    GPIO.output(21,False)
    GPIO.output(20,True)

def backward():
    #Left Wheel
    GPIO.output(12,True)
    GPIO.output(16,False)
    #Right Wheel
    GPIO.output(21,True)
    GPIO.output(20,False)

def left():
    #Left Wheel
    GPIO.output(12,True)        #Moving Backward
    GPIO.output(16,False)
    #Right Wheel
    GPIO.output(21,False)       #Moving Forward
    GPIO.output(20,True)

def right():
    #Left Wheel
    GPIO.output(12,False)       #Moving Forward
    GPIO.output(16,True)
    #Right Wheel
    GPIO.output(21,True)        #Moving Backward
    GPIO.output(20,False)

def stop():
    #Left Wheel
    GPIO.output(12,False)
    GPIO.output(16,False)
    #Right Wheel
    GPIO.output(21,False)
    GPIO.output(20,False)


GPIO.setup(14,GPIO.IN) # Set pin 14 to Input to get input from IR Sensor

try:
    while True:
        forward()
        a=GPIO.input(14)    #Taking input from IR sensor
        if(not a):          #In case of interruption Body of if is executed
            stop()
            time.sleep(0.5)
            backward()
            time.sleep(1)
except:
    KeyboardInterrupt()     #Press Ctrl+C or Ctrl+Z for Keyboard Interrupt
GPIO.cleanup()              #Stops all Input and Output

'''
   #Moving in all directions in a loop

   while True:
    forward()
    time.sleep(3)
    backward()
    time.sleep(3)
    left()
    time.sleep(3)
    right()
    time.sleep(3)
    stop()
    time.sleep(2)    

'''
