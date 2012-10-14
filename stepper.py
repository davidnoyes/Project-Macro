import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

WaitTime = 0.001
StepPins = [24,25,8,7]

for pin in StepPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,False)

StepCount = 8
Seq = []
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

StepCounter = 0
while 1==1:
	
	for pin in range(0,4):
		xpin = StepPins[pin]
		if Seq[StepCounter][pin] != 0:
			GPIO.output(xpin, True)
		else:
			GPIO.output(xpin, False)
	
	StepCounter += 1

	if (StepCounter == StepCount):
		StepCounter = 0
	if (StepCounter < 0):
		StepCounter = StepCount

	time.sleep(WaitTime)
