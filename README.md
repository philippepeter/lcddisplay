# lcddisplay
Docker image to display a string on an LCD screen of an arduino using the serial port.

## Electronic wires:
[Arduino liquid crystal display](https://www.arduino.cc/en/Tutorial/LiquidCrystalDisplay)

## Arduino code
Created from the the Arduino example: LiquidDisplay->SerialDisplay

[The code](https://github.com/philippepeter/lcddisplay/blob/master/display.arduino)

## Command
`docker run --device=/dev/[USB_DEVICE] [DOCKER_IMAGE_NAME] "[STRING_TO_DISPLAY]"`

For example on a raspberrypi:
`docker run --device=/dev/ttyACM0 lcddisplay "Hello world!"`

# Netatmo reader

## Raspberry installation

`sudo apt-get update`
`sudo apt-get install python3`
`sudo apt-get install python-pip`
`sudo pip install pySerial`
`sudo pip install requests`


## Python script
```python
import requests
import serial
import time
import sys

payload = {'grant_type': 'password',
           'username': "[MAIL]",
           'password': "[PASSWORD]",
           'client_id':"[ID]",
           'client_secret': "[SECRET]"
           }
try:
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    refresh_token=response.json()["refresh_token"]
    scope=response.json()["scope"]
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

params = {
    'access_token': access_token,
    'device_id': '[DEVICE_MAC]'
}

try:
    response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    devices = data["devices"]
    device = devices[0]
    dashboard = device["dashboard_data"]
    temp = dashboard["Temperature"]
    print(temp)
    modules = device["modules"]
    dashboard_ext = modules[0]["dashboard_data"]
    temp_ext = dashboard_ext["Temperature"]

    value = "Out=" + str(temp_ext) + " In=" + str(temp)

    ser = serial.Serial('/dev/ttyACM0',9600)
    time.sleep(2)
    ser.write(value.encode())


except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

```
## Cron table and rc.local

`sudo crontab -e`

add 
`*/10 * * * * python /home/pi/run.py`

`sudo vi /etc/rc.local`

add
`sudo python /home/pi/run.py`

before exit 0


