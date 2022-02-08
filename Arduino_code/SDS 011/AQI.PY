from sds011 import SDS011 

import time 

s = SDS011('/dev/tty.usbserial-1120')
s.sleep (sleep = False) 


while True : 
    val = s.query()
    print(s) 
    time.sleep(2)


s.sleep() 
print(waitTime) 
time.sleep(waitTIme)