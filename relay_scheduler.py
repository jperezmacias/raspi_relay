import sched, time
import RPi.GPIO as GPIO
import datetime
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)    #RESET
GPIO.setup(27, GPIO.OUT)    #OPEN
GPIO.setup(22, GPIO.OUT)    #CLOSE

GPIO.setwarnings(False)

print "LED on"
GPIO.output(27,GPIO.LOW)

def action():
    GPIO.output(27,GPIO.LOW)

# Set up scheduler
#s = sched.scheduler(time.localtime, time.sleep)
# Schedule when you want the action to occur
#s.enterabs(time.strptime('Sat Sep 01 15:36:00 2019'), 0, action)
# Block until the action has been run
GPIO.output(27,GPIO.LOW)

#s.run()
