import socket
import RPi.GPIO as GPIO
HEADERSIZE = 10
host = '192.168.1.105'
port = 1243

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm2=GPIO.PWM(12, 50)
pwm.start(0)
pwm2.start(0)

#b1 = bytearray('----')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#

s.connect((host,port))
    
while True:
    msg = s.recv(12)
    
    john = msg.decode("utf-8")
    #j = s.recvmsg_into([b1,b1,b1])
    #print(john)
    if john.startswith('('):
        #print(john[1:11])
        #print(john[7:11])
        list1 = john.split(',',1)
        x = str(list1[0])
        x1 = x.replace(',','')
        x1 = x1.replace('(','')
        y = str(list1[1])
        y1 = y.replace(',','')
        y1 = y1.replace(')','')
        pwm.ChangeDutyCycle(int(x1)/float(100))
        pwm2.ChangeDutyCycle(int(y1)/float(30)+3)
       # y = list[1]
        #print(x)
        #print(int(x1))
       # print(int(y1))
        #print(list1[1])
    #print(int(john))

