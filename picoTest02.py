# Picocon Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python picoTest02.py


import time, picocon

speed = 15 # 0 is stopped, 100 is fastest
picocon.init()

# main loop
try:
    while True:
        picocon.forward(speed)
        print 'Forward'
        time.sleep(3)
        picocon.reverse(speed)
        print 'Reverse'
        time.sleep(3)
        picocon.spinRight(speed)
        print 'Spin Right'
        time.sleep(3)
        picocon.spinLeft(speed)
        print 'Spin Left'
        time.sleep(3)
        picocon.stop()
        print 'Stop'
        time.sleep(3)

except KeyboardInterrupt:
    print

finally:
    picocon.cleanup()
    
