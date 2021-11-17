''' 
A Testing script for the Adafruit Ultimate GPS module 

This script is built to measure the delays involved in communicating
with the GPS module to determine constraints in design of the controller.

Author(s): Jaidon Lybbert
Date     : Nov 17, 2021
'''
import serial
from datetime import datetime, timedelta
import ntplib

class Reciever: 

    def __init__(self):
        self.port = serial.Serial("COM4", 9600, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        
        # OS time isn't accurate enough, so have to synchronize with ntp server
        # Offset is the time that the OS time is offset from 'real' UTC time, accounting for roundtrip transmission time
        ntp_client = ntplib.NTPClient()
        ntp_response = ntp_client.request('europe.pool.ntp.org', version=3)
        self.time_offset = ntp_response.offset

    def recv_data(self):
        return self.port.readline()

    def parse_data(self):
        print(self.recv_data())
        print(datetime.utcnow() + timedelta(seconds=self.time_offset))


def main():
    reciever = Reciever()

    while(True):
        reciever.parse_data()


if __name__ == '__main__':
    main()
