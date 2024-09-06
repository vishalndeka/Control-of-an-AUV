import numpy as np
import time, math
from pyfirmata import Arduino, SERVO
from XboxController import XboxController

def init_connections():
    port = 'COM8' # 'COM7'
    pin = 9
    board = Arduino(port)
    board.digital[pin].mode = SERVO
    return board, pin

def servo_signal(board, pin, g_input):
    val = np.max([0, np.int32(g_input[0]*180)])
    print(val)
    board.digital[pin].write(np.int32(val))



if __name__ == '__main__':
    joy = XboxController()
    board, pin = init_connections()
    while True:
        servo_signal(board, pin, joy.read())
        # servo_signal(board, pin, joy.read())