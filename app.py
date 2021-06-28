#!/usr/bin/env python
import os.path
import re
from flask import Flask

app = Flask(__name__)

@app.route('/')
def temperature():
    try:
        with open("/sys/bus/w1/devices/28-01193a8403e8/w1_slave") as f:
            content = f.read().splitlines()
            regex = re.match(r'.+t=(\d+)', content[1])
            temperature = str(round(float(regex.group(1)) / 1000, 1))
            return temperature
    except Exception as e:
        print(e)
        return 'ERROR: Temperature cannot be read.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

