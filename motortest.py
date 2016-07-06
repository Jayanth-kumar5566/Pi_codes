import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

in1_pin=2
in2_pin=5
in3_pin=2
GPIO.setup(in1_pin,GPIO.OUT)
GPIO.setup(in2_pin,GPIO.OUT)
GPIO.setup(in3_pin,GPIO.OUT)
print "Turning on motor"
GPIO.output(in1_pin,GPIO.HIGH)
GPIO.output(in3_pin,GPIO.HIGH)
GPIO.output(in2_pin,GPIO.LOW)
sleep(2)
print "Stoping motor"
GPIO.output(in3_pin,GPIO.LOW)
GPIO.cleanup()
