'''
Created on 16.01.2017

@author: Enrico
@note: Starts the Robot and make JoypadMovement possible
'''
from .Engine import Engine
from .xbox import Joystick

EngineLeft = Engine(2,3)
EngineRight = Engine(4,5)
hatch1 = Engine(6,7)
hatch2 = Engine(8,9)
joy = Joystick()

def motorMovementFromCords(x,y):
    #getting speed trough y
    speed = abs(y)    
    # no move if nothing pressed
    if x==0.0 and y==0.0:
        EngineLeft.stop()
        EngineRight.stop()
    #Forward    
    if y>0.0:
        #forward right
        if x>0 and x<1: 
            EngineLeft.forward(speed * 100 )
            EngineRight.forward((1-x) * (speed*100))
        if x==1: 
            EngineLeft.forward(100)
            EngineRight.backward(100)
            
        #forward left
        if x<0 and x>-1: 
            EngineLeft.forward((1+x) *(speed* 100))
            EngineRight.forward(speed * 100)
        if x==-1: 
            EngineLeft.backward(100)
            EngineRight.forward(100)
    #Backward           
    if y<0.0:
        #Backward right
        if x>0 and x<1:
            EngineLeft.backward(1 * (speed* 100))
            EngineRight.backward((1-x) *(speed* 100))
        if x==1: 
            EngineLeft.backward(100)
            EngineRight.forward(100)
            
        #Backward left
        if x<0 and x>-1: 
            EngineLeft.backward((1+x) * (speed * 100))
            EngineRight.backward(speed * 100 )
        if x==-1: 
            EngineLeft.forward(100)
            EngineRight.backward(100)       
       

def JoypadMovement():
    
    while(True):
        while (joy.dpadUp()):
            EngineLeft.forward(100)
            EngineRight.forward(100)
        while (joy.dpadDown()):
            EngineLeft.backward(100)
            EngineRight.backward(100)
        while (joy.dpadLeft()):
            EngineLeft.backward(50)
            EngineRight.forward(100)
        while (joy.dpadRight()):
            EngineLeft.backward(50)
            EngineRight.forward(100)
            
        x, y = joy.leftStick()
        motorMovementFromCords(x,y)
            
        if(joy.Back()):
            joy.close()
            print ("movement stopped, shut down program")
            exit()

if __name__ == '__main__':
    print ("Robot is Ready")
    while(True):
        if(joy.Start()):
            print ("Robot movement with Xbox Controller ")
            JoypadMovement()    
    pass