# Print the increments of the left and right motor.
# Now using the LegoLogfile class.
# 01_b_print_motor_increments.py
# Claus Brenner, 07 NOV 2012
from lego_robot import LegoLogfile
from pylab import *

if __name__ == '__main__':

    logfile = LegoLogfile()
    logfile.read("robot4_motors.txt")

    plot(logfile.motor_ticks)
    show()