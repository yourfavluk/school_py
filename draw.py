from picoboy import PicoBoy
import time
import random
import _thread

pb = PicoBoy()

x=64
y=32

pb.fill(0)

while(True):
    if(pb.JOY_UP.value()==0):
        y=y-1
    
    if(pb.JOY_DOWN.value()==0):
        y=y+1

    if(pb.JOY_LEFT.value()==0):
        x=x-1

    if(pb.JOY_RIGHT.value()==0):
        x=x+1

    if(pb.JOY_CENTER.value()==0):
        pb.fill(0)
    
    else:
       pb.pixel(x,y,1)
       
       time.sleep_ms(50)
       
       pb.show()
