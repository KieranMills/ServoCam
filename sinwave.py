import RPi.GPIO as GPIO
import math
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm2=GPIO.PWM(12, 50)
pwm.start(0)
pwm2.start(0)

t1 = 7
j = 0.1
t = 1

while t1>3:
    
    pwm.ChangeDutyCycle(5*math.sin(2*t1)+7) # left -90 deg position
   # pwm2.ChangeDutyCycle(math.sin(2*t1)+7) # left -90 deg position
    print(t1)
    sleep(0.2*j)
    t1 = t1 +0.2
    print()
    #t = t+ 0.1
    #print(t,t1)
    
    #print("feels like im wearin, Nothin at All!")
pwm.stop()
GPIO.cleanup

