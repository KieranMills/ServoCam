


import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm2=GPIO.PWM(12, 50)
pwm.start(0)
pwm2.start(0)

t1 = 0
j = 0.1
t = 1

while True:
    
    #pwm.ChangeDutyCycle(t) # left -90 deg position
    pwm2.ChangeDutyCycle(t1) # left -90 deg position

    sleep(0.4*j)
    t1 = t1 +0.1
    t = t+ 0.1
    #print(t,t1)
    #print("feels like im wearin, Nothin at All!")
pwm.stop()
GPIO.cleanup

