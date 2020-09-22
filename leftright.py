import RPi.GPIO as GPIO
from time import sleep
from pynput import mouse

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm2=GPIO.PWM(12, 50)
pwm.start(0)
pwm2.start(0)


j = 0.1
t = 1


def on_move(x, y):
    
    print('Pointer moved to {0}'.format(
        (x/100)))
    pwm.ChangeDutyCycle(x/100)
    sleep(0.4*j)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False
    

    
    
with mouse.Listener(
        on_move=on_move,
        on_click=on_click
        ) as listener:
    listener.join()    


    
    #pwm.ChangeDutyCycle(t) # left -90 deg position
    #pwm2.ChangeDutyCycle(t1) # left -90 deg position

    #sleep(0.4*j)
    
    #t = t+ 0.1
    #print(t)
    #print("feels like im wearin, Nothin at All!")
#pwm.stop()
#GPIO.cleanup