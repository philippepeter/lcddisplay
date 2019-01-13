import requests
import serial
import time
import sys

payload = {'grant_type': 'password',
           'username': "[MAIL]",
           'password': "[PASSWORD]",
           'client_id':"[CLIENID]",
           'client_secret': "[SECRET]"
           }
try:
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    refresh_token=response.json()["refresh_token"]
    scope=response.json()["scope"]
    print("Your access token is:", access_token)
    print("Your refresh token is:", refresh_token)
    print("Your scopes are:", scope)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

params = {
    'access_token': access_token,
    'device_id': '[DEVICE ID]'
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
    print(value)

    ser = serial.Serial('/dev/ttyACM0',9600)
    time.sleep(2)
    ser.write(value.encode())    


except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)


