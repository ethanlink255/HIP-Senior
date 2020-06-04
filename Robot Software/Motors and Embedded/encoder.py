import RPi.GPIO

GPIO.setmode(GPIO.BOARD)

CLKpin = 1
DTpin = 1

LSTpin = None
aVal = None
bCW = None

encoderCount = 0

GPIO.setup(CLKpin, GPIO.IN)
GPIO.setup(DTpin, GPIO.IN)

LSTpin = GPIO.input(CLKpin)

while True:
    aVal = GPIO.input(CLKpin)
    if aVal != LSTpin:
        if(GPIO.input(DTpin) != aVal):
            encoderCount += 1
            bCW = True
        else:
            bCW = False
            encoderCount -= 1
        print("Rotated: ")

        if(bCW):
            print("Clockwise")
        else:
            print("CounterClockwise")

        print("Encoder Position: " + str(encoderCount))

    LSTpin = aVal
