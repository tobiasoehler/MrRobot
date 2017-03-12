'''
Created on 16.01.2017

@author: tobiasoehler
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Engine:
    def __init__(self, pinForward, pinBackward, pinEnable):
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.enablePin = pinEnable

    def forward(self, speed):
        GPIO.setup(self.pinBackward,GPIO.OUT)
        GPIO.setup(self.pinForward,GPIO.OUT)
        GPIO.output(self.pinBackward,GPIO.LOW)
        GPIO.output(self.pinForward,GPIO.HIGH)
        p = GPIO.PWM(self.pinEnable, 100.0).start(speed)
        p.start(speed)

    def backward(self, speed):
        GPIO.setup(self.pinBackward,GPIO.OUT)
        GPIO.setup(self.pinForward,GPIO.OUT)
        GPIO.output(self.pinBackward,GPIO.HIGH)
        GPIO.output(self.pinForward,GPIO.LOW)
        p = GPIO.PWM(self.pinEnable, 100.0).start(speed)
        p.start(speed)

    def stop(self):
        GPIO.setup(self.pinBackward,GPIO.OUT)
        GPIO.setup(self.pinForward,GPIO.OUT)
        GPIO.output(self.pinEnable,GPIO.LOW)
        GPIO.output(self.pinForward,GPIO.LOW)
        GPIO.output(self.pinBackward,GPIO.LOW)
