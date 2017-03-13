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
        self.pinEnable = pinEnable
        GPIO.setup(self.pinBackward,GPIO.OUT)
        GPIO.setup(self.pinForward,GPIO.OUT)
        GPIO.setup(self.pinEnable,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pinEnable, 100)

    def forward(self, speed):
        GPIO.output(self.pinBackward,GPIO.LOW)
        GPIO.output(self.pinForward,GPIO.HIGH)
        self.pwm.start(speed)

    def backward(self, speed):
        GPIO.output(self.pinBackward,GPIO.HIGH)
        GPIO.output(self.pinForward,GPIO.LOW)
        self.pwm.start(speed)

    def stop(self):
        GPIO.output(self.pinEnable,GPIO.LOW)
        GPIO.output(self.pinForward,GPIO.LOW)
        GPIO.output(self.pinBackward,GPIO.LOW)
