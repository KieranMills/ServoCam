
from __future__ import division
import RPi.GPIO as GPIO
channel = 23
import time
# Import the PCA9685 module.
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

import socket
#import RPi.GPIO as GPIO
import struct
HEADERSIZE = 10
host = '192.168.1.11'
#change your ip here to the computer you use.
port = 80

#PIO.setmode(GPIO.BOARD)
#PIO.setup(11, GPIO.OUT)
#PIO.setup(12, GPIO.OUT)

#=GPIO.PWM(11, 50)
#=GPIO.PWM(12, 50)
# x.start(0)
# y.start(0)
resx = 1920
resy = 1200

#b1 = bytearray('----')

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
        motor_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
st = struct.Struct('I I')
print('successful connection')
while True:
    msg = s.recv(8)
    coords = st.unpack(msg)
    #x.ChangeDutyCycle(coords[0]/float(100))
    #y.ChangeDutyCycle(coords[1]/float(30)+3)
    x = coords[0]   # resx = your screen resolution x
    y = coords[1]  # resy = your screen resolution y
    #print(x)
    #print(y)
    value = int(x/float(7)+250)
    valuey = int(y/float(5))+140
    pwm.set_pwm(15, 0, value)
    print(value,valuey)
    pwm.set_pwm(0, 0, int(y))
    #print('input y:', valuey)
    #print("{} {} " . format(coords[0], coords[1]))

#    if speed < 100:

       #x.ChangeDutyCycle(speed)
       #y.ChangeDutyCycle(speedy)
       #this was changed for marcus
