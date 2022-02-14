import serial
import sys
import time
arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:
    i = input("enter input: ").strip()
    if i == "done":
        print('Finished')
        break
    arduino.write(i.encode())
    time.sleep(0.5)
    print(arduino.readline().decode('ascii'))


'''
print (arduino.readline())
#arduino.write(bytes('pysidasdasdasdadsadsae','utf-8'))
i = "on"
arduino.write(i.encode())

arduino.close()
'''