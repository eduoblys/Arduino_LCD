import serial
import sys
import time
import requests

arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:

    i = input("enter input: ").strip()
    if i == "done":
        print('Finished')
        print(r)
        break
        time.sleep(5)
    r = requests.get('https://api.chucknorris.io/jokes/random', data={'key': 'value'})

    r.text
    print(r.text)

    arduino.write(r.encode())
    time.sleep(5.5)
    print(arduino.readline().decode('ascii'))
    print(r)

'''
print (arduino.readline())
#arduino.write(bytes('pysidasdasdasdadsadsae','utf-8'))
i = "on"
arduino.write(i.encode())

arduino.close()
'''