# Picocon Motor Test - no library
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python picoTest01.py


import time, RPi.GPIO as GPIO

# Pins 24, 26 Right Motor
# Pins 19, 21 Left Motor
R1 = 24
R2 = 26
L1 = 19
L2 = 21

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

#set motor pins as outputs
GPIO.setup(L1, GPIO.OUT)    # pin 19 is left motor A
GPIO.setup(L2, GPIO.OUT)    # pin 21 is left motor B
GPIO.setup(R1, GPIO.OUT)    # pin 24 is right motor A
GPIO.setup(R2, GPIO.OUT)    # pint 26 is right motor B


# main loop
try:
    while True:
        # move forward
        GPIO.output(L1, 1)
        GPIO.output(L2, 0)
        GPIO.output(R1, 1)
        GPIO.output(R2, 0)
        print 'Forward'
        time.sleep(3)

        # move backward
        GPIO.output(L1, 0)
        GPIO.output(L2, 1)
        GPIO.output(R1, 0)
        GPIO.output(R2, 1)
        print 'Reverse'
        time.sleep(3)

        # spin right
        GPIO.output(L1, 1)
        GPIO.output(L2, 0)
        GPIO.output(R1, 0)
        GPIO.output(R2, 1)
        print 'Spin Right'
        time.sleep(3)

        # spin left
        GPIO.output(L1, 0)
        GPIO.output(L2, 1)
        GPIO.output(R1, 1)
        GPIO.output(R2, 0)
        print 'Spin Left'
        time.sleep(3)

        # stop
        GPIO.output(L1, 0)
        GPIO.output(L2, 0)
        GPIO.output(R1, 0)
        GPIO.output(R2, 0)
        print 'Stop'
        time.sleep(3)

except KeyboardInterrupt:
    print

finally:
    GPIO.cleanup()
    
