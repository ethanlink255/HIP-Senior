import serial
from enum import Enum
import struct 


class Leg(Enum):
    TOP_LEFT = "/dev/tty/USB0"
    TOP_RIGHT = "/dev/tty/USB0"
    BOTTOM_LEFT = "/dev/tty/USB0"
    BOTTOM_RIGHT = "/dev/tty/USB0"





class Protocol():

 
    def crc8(self, data):
        crc = 0
        for i in range(len(data)):
            byte = data[i]
            for b in range(8):
                fb_bit = (crc ^ byte) & 0x01
                if fb_bit == 0x01:
                    crc = crc ^ 0x18
                crc = (crc >> 1) & 0x7f
                if fb_bit == 0x01:
                    crc = crc | 0x80
                byte = byte >> 1
        return crc
        

    def __init__(self, deg, joint_type):
        self.message = struct.pack("QQ", deg, joint_type)
        sum = struct.pack("Q", self.crc8(self.message))
        self.message += sum


class Comms():

    
    def __init__(self):
        self.TL_Serial = serial.Serial(Leg.TOP_LEFT)
        self.TR_Serial = serial.Serial(Leg.TOP_RIGHT)
        self.BL_Serial = serial.Serial(Leg.BOTTOM_LEFT)
        self.BR_Serial = serial.Serial(Leg.BOTTOM_RIGHT)
        
    def send_message(self, serial_port, message):
        print("W")

  



message = Protocol(18, 1).message
print(message)
