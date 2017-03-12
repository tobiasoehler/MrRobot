#from gpiozero import Motor
#import RPi.GPIO as GPIO
from camera import Camera
import time


camera = Camera()

while True:
	print(time.strftime("%d.%m.%Y %H:%M:%S"))
	(preRadius, preCenter, preColor) = (camera.getBiggestCenter([(95,100,100), (95,100,100)], [(110, 255, 255), (110, 255, 255)]))
	print (preRadius)
	print (preCenter)
	print (preColor)
