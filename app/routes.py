from flask import Flask
from flask import render_template
from flask import jsonify
from main import Balance

app = Flask(__name__)




@app.route("/")
def home():
	return render_template("home.html")

@app.route("/getbitcoin/")
def getbitcoin():

	# balance = arduino.readline()
	return render_template("getbitcoin.html", balance = Balance.balance)

# @app.route("/background_process/")
# def background_process():
# 	value = arduino.readline()
# 	balance = arduino.readline()
	

if __name__ == "__main__":
	app.run(debug = True)