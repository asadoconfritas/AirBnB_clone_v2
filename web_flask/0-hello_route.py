#!/usr/bin/python3
"""py3 flask web app"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return('Hello HBNB!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)