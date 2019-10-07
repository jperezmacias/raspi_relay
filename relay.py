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
#GPIO.output(27,GPIO.LOW)
#GPIO.output(27,GPIO.LOW)

time.sleep(1)
print "LED off"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
