import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT

GPIO.setup(11, GPIO.OUT) ## Setup GPIO pin 11 to OUT

## Define function named Blink()
def Blink7(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(7, True) ## Turn on GPIO pin 7
        print "GPIO 7 turned true"
        time.sleep(speed) ## Wait
        GPIO.output(7, False) ## Switch off GPIO pin 7
        print "GPIO 7 turned false"
        time.sleep(speed) ## Wait
    print "Loop for blink 7 done" ## When loop is complete, print "Done"

def Blink11(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(11, True) ## Turn on GPIO pin 7
        print "GPIO 11 turned true"
        time.sleep(speed) ## Wait
        GPIO.output(11, False) ## Switch off GPIO pin 7
        print "GPIO 11 turned false"
        time.sleep(speed) ## Wait
    print "Loop for blink 11 done" ## When loop is complete, print "Done"

## Prompt user for input
# iterations = raw_input("Enter the total number of times to blink: ")
# speed = raw_input("Enter the length of each blink in seconds: ")

iterations = 1 
speed = 1

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
# Blink(int(iterations),float(speed))
        
bulbno = raw_input("Enter the bulb to be toggled: ")

if bulbno == "1" :
    Blink7(int(iterations),float(speed))
    print "Bulb on GPIO 7 toggled"
elif bulbno=="2" :
    Blink11(int(iterations),float(speed))
    print "Bulb on GPIO 11 toggled"
else :
    print "nothing done"


GPIO.cleanup()
print "GIPO cleanup done"
print "program exited"
