# import the necessary packages
import cv2

class Camera:

	def __init__ (self):
		self.camera = cv2.VideoCapture(0)

	def getPictureAsHsv(self):
		(grabbed, self.frame) = self.camera.read()
		self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

	def getCenterForColorAndRadius(self, colorLower, colorUpper):
		mask = cv2.inRange(self.hsv, colorLower, colorUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
								cv2.CHAIN_APPROX_SIMPLE)[-2]
		self.center = (-1,-1)
		if len(cnts) > 0:
			c = max(cnts, key=cv2.contourArea)
			((x, y), self.radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			self.center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	def getBiggestCenter(self, colorLower, colorUpper):
		self.getPictureAsHsv()
		preRadius = -1
		preCenter = -1
		preColor = -1
		i = 0
		while i <= len(colorLower)-1:
			self.getCenterForColorAndRadius(colorLower[i], colorUpper[i])
			if (self.radius > preRadius):
				preRadius = self.radius
				preCenter = self.center
				preColor = colorLower[i]
			i = i + 1

		return preRadius, preCenter, preColor
