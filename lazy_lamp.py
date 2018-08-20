import RPi.GPIO as GPIO
import os

from flask import Flask, request, render_template, redirect, url_for, flash, make_response
app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(37, GPIO.OUT)

@app.route('/', methods=['GET'])
def lazy_lamp():
	if request.method == 'GET':
		return render_template('switch.html')

@app.route('/switch_on', methods=['POST'])
def lightON():
	if request.method == 'POST':
		GPIO.output(37, GPIO.LOW)
	return render_template('switch.html')

@app.route('/switch_off', methods=['POST'])
def lightOFF():
        if request.method == 'POST':
                GPIO.output(37, GPIO.HIGH)
	return render_template('switch.html')


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run(app.run(host=os.getenv('IP', '192.168.0.18'), port=int(os.getenv('PORT', 8080))))

