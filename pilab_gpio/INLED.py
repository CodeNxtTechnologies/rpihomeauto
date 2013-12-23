import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.setup(11, GPIO.IN , initial=GPIO.LOW) ## setup gpio pin 11 to in
GPIO.output(7, False)

## Define function named Blink()
def Blink(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(7, True) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(7, False) ## Switch off GPIO pin 7
        time.sleep(speed) ## Wait
    print "Done" ## When loop is complete, print "Done"

    
## Prompt user for input
# iterations = raw_input("Enter the total number of times to blink: ")
# speed = raw_input("Enter the length of each blink in seconds: ")
iterations=1
speed=5
## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters

for j in range(0,20):
    if GPIO.input(11) :
        Blink(int(iterations),float(speed))
    else:
        print "Gpio input on pin 11 at end of program is :" + str(GPIO.input(11))    
    time.sleep(3)
    j=j+1

try:
    GPIO.cleanup()
except:
    print "cleanup failed"

print "program exited"

