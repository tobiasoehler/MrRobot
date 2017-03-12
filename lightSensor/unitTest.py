from lightSensor import LightSensor

try:
    lightSensor = LightSensor(7)
    while True:
        print lightSensor.rc_time()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
