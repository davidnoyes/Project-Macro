import smbus
import sys
import getopt
import time

bus = smbus.SMBus(0)

address = 0x20 #I2C address of MCP23017
bus.write_byte_data(address,0x00,0x00) #Set all of bank A to output
bus.write_byte_data(address,0x01,0x00) #Set all of bank B to output

WaitTime = 0.0005

StepCount = 8
Seq = []
Seq = range(0, StepCount)
Seq[0] = 1 #[0,0,0,1]
Seq[1] = 3 #[0,0,1,1]
Seq[2] = 2 #[0,0,1,0]
Seq[3] = 6 #[0,1,1,0]
Seq[4] = 4 #[0,1,0,0]
Seq[5] = 12 #[1,1,0,0]
Seq[6] = 8 #[1,0,0,0]
Seq[7] = 9 #[1,0,0,1]


def set_data(data,bank):
	if bank == 1:
		bus.write_byte_data(address, 0x12, data)
	else:
		bus.write_byte_data(address, 0x13, data)

def main():
	StepCounter = 0

	while 1==1:
		set_data(Seq[StepCounter],1)
		StepCounter += 1

		if (StepCounter == StepCount):
			StepCounter = 0
		if (StepCounter < 0):
			StepCounter = StepCount

		time.sleep(WaitTime)

if __name__ == "__main__":
	main()
