import RPi.GPIO as GPIO
import time

class lightSensor:
    def __init__ (self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin

    def rc_timeShadow (self):
        count = 0
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(self.pin, GPIO.IN)
        while (GPIO.input(self.pin) == GPIO.HIGH):
            count += 1

        return count

    def rc_timeLight (self):
        count = 0
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(self.pin, GPIO.IN)
        while (GPIO.input(self.pin) == GPIO.LOW):
            count += 1

        return count

    def high (self):
        GPIO.setup(self.pin, GPIO.IN)
        if (GPIO.input(self.pin) == 0):
            return "true"
        else:
            return "false"
        #return GPIO.input(self.pin)
        
try:
    sensor = lightSensor(11)
    while True:
        print sensor.high()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

