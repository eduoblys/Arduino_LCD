import serial
import sys
import time
import requests
import json
arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:
    r = requests.get('https://api.chucknorris.io/jokes/random', data={'key': 'value'})
    json = r.json()
    print(json["value"])
    arduino.write(json["value"].encode())
    time.sleep(8.5)
    arduino.write("e\ncoding\nssss sssda ".encode())
    time.sleep(8.5)

