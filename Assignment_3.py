#python code for blinking LED and traffic lights for Respberry pi
#python code for blinking LED
import RPi.GPIO as GPIO # import pi GPIO library
from time import sleep #import the sleep function from the time module
GPIO. setwarning(false) #Ignore warning for now
GPIO.setmode(GPIO.BOARD) # use physical pin numbering
GPIO. setup(8, GPIO.OUT, initial=GPIO.LOW) # set pin 8 be an output pin and set initial value to low
(off)
while True: # Run foreveR
    GPIO.output(8,GPIO.HIGH)# Turn on
    sleep(1) # sleep for 1 second
    GPIO. output(8, GPIO.LOW) # Turn off
    sleep(1) # sleep for 1 second
    #python code for Traffic Light
    import Rpi.GPIO as GPIO
    import time
    import signal
    import sys
    # setup
    GPIO.setup(GPIO.BCM)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    #Turn off all lights when user ends demo
    def allLightsoff(signal,frame):
        GPIO.output(9,False)
        GPIO.output(10,False)
        GPIO.output(11,False)
        GPIO.cleanup()
        sys.exit(0)
        signal.signal(signal.SIGINT,allLightsoff)
        # loop forever
        while True:
            #Red and amber
            GPIO.output(10,True)
            time.sleep(1)
            #Green
            GPIO.output(9,False)
            GPIO.output(10,False)
            GPIO.output(11,True)
            time . sleep(5)
            #Amber
            GPIO.output(11,False)
            GPIO.output(10,True)
            time.sleep(2)
            #Amber off(red comes on ar top of loop)
            GPIO.output(10,false)
    
     




























;
