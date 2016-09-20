#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
app = Flask(__name__)

# Since v0.7, static content is automatically served from "static/". See the
#   static_folder and static_url_path arguments of flask.Flask()


@app.route("/")
def index():
    return \
        "<h1>Garage Controller</h1>" \
        "<form action=\"/toggle_door\"><input type=\"submit\" value=\"Toggle Door\" /></form>"


@app.route("/toggle_door")
def toggle_door():
    GPIO.output(11, 0)
    sleep(0.5)
    GPIO.output(11, 1)
    return "Done."


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([11, 12], GPIO.OUT, initial=GPIO.HIGH)


def term():
    GPIO.cleanup()


def run():
    # Enabling Flask debugging in production stops request threads on exception
    #   to allow debugger connections. This also happens for abruptly closed
    #   connections hat result in "socket.error: [Errno 32] Broken pipe".
    # app.debug = True
    app.run(host="localhost", port=8000)


def main():
    init()
    run()
    term()


if __name__ == "__main__":
    main()
