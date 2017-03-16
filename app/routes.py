from flask import Flask
from flask import render_template
import serial

app = Flask(__name__)


arduino = serial.Serial("/dev/tty.usbmodem411", 9600, timeout=1) # Connect to Arduino  mit timeout wird einfach aufgehort zu laden, wenn es zu lange dauert




@app.route("/")
def home():
	return render_template("home.html")

@app.route("/getbitcoin/")
def getbitcoin():

	balance = arduino.readline()
	print(balance.rstrip())

	return render_template("getbitcoin.html", balance = balance)

	

if __name__ == "__main__":

	app.run(port=5000, host='0.0.0.0', debug = True, use_reloader=True)

