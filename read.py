import serial
import time

ser = serial.Serial("COM15", 15200)
while True:
     cc=str(ser.readline())
     print(cc[2:][:-5])

"""
ser = serial.Serial('COM15')
print(ser.name)

line = ser.readline()


for line in ser.read():
    print(line)
"""