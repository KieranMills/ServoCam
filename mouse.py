from pynput import mouse

x2 = 0
y2 = 0

def on_move(x, y):
    
   # print('Last Pointer {0}'.format(
       # (x2, y2)))
    
  
    
    print('Pointer moved to {0}'.format(
        (x/float(100), y/float(100))))
    
   # x2 = x
#y2 = y
    
    #print('Pointer moved2 to {0}'.format(
       # (x2, y2)))
    
   
    
    
   



def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click
        ) as listener:
    listener.join()