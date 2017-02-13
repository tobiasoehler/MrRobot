'''
Created on 16.01.2017

@author: tobiasoehler
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Engine:
    def __init__(self, pinForward, pinBackward):
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        GPIO.setup(self.pinBackward,GPIO.OUT)
        GPIO.setup(self.pinForward,GPIO.OUT)

    def forward(self, speed):
        GPIO.output(self.pinBackward,GPIO.LOW)
        p = GPIO.PWM(self.pinForward,100.0).start(speed)
        p.start(speed)
        
    def backward(self, speed):
        GPIO.output(self.pinForward,GPIO.LOW)
        p = GPIO.PWM(self.pinBackward,100.0)
        p.start(speed)
        
    def stop(self):
        GPIO.output(self.pinForward,GPIO.LOW)
        GPIO.output(self.pinBackward,GPIO.LOW)
       
