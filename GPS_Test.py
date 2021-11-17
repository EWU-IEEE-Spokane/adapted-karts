''' 
A Testing script for the Adafruit Ultimate GPS module 

This script is built to measure the delays involved in communicating
with the GPS module to determine constraints in design of the controller.

Author(s): Jaidon Lybbert
Date     : Nov 17, 2021
'''
import serial

class Reciever: 

    def __init__(self):
        self.port = serial.Serial("COM4", 9600, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

    def recv_data(self):
        return self.port.readline()

    def parse_data(self):
        print(self.recv_data())


def main():
    reciever = Reciever()

    while(True):
        reciever.parse_data()


if __name__ == '__main__':
    main()
