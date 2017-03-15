#!/usr/bin/python

import serial
import requests
from flask import Flask, render_template

arduino = serial.Serial("/dev/tty.usbmodem411", 9600) # Connect to Arduino

url = "http://localhost:3000/change" # Endpoint to update balance

auth = "qwerty" # Auth key that matched the one in the config for the app

app = Flask(__name__) 


class Balance():
    value = arduino.readline()
    balance = arduino.readline()
    print value.rstrip()
    print balance.rstrip()

    
def update(balance):

    print(str(balance) + "p")

    headers = {"Content-type": "application/json", "Accept": "text/plain"}

    r = requests.post(url, headers=headers, json={"auth": auth, "balance": balance}) # Send request off to server

    if r.status_code == 201:

        print("Sent update!")

    elif r.status_code == 401:

        print("Auth key is wrong!")

    else:

        print("Failed to update app for some unknown reason!")

    return True


if __name__ == "__main__":

    app.run(debug=True)

    print("Running...") # Let's do this! Whooo

    while True:

        value = arduino.readline() # Read line from the Arduino

        try:

            value.split() # Remove any whitespace

            balance = int(value) # Turn it into an int

            update(balance)

        except:

            pass # Shhh nothing happened...






# app.run(debug = True, port=8000, host='0.0.0.0')

























