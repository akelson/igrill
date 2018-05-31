from flask import Flask
import json
import datetime
from subprocess import Popen, PIPE
from igrill import IGrillV2Peripheral

ADDRESS = 'D4:81:CA:20:4E:8E'

class Server(object):
    def __init__(self):
        self.periph = None
        self.scan_proc = None
        self.scan_data = '{"status":"not_started"}'

    def scan(self):
        if self.scan_proc == None:
            self.scan_proc = Popen(
                ["sudo", "/usr/bin/python", "scanner.py"],
                stdout=PIPE, stderr=PIPE)
            self.scan_data = '{"status":"runing"}'
        return "ok"

    def scan_result(self):
        if self.scan_proc and None != self.scan_proc.poll():
            self.scan_data, err = self.scan_proc.communicate()
            print err
            self.scan_proc = None
        return self.scan_data

    def connect(self):
        self.periph = IGrillV2Peripheral(ADDRESS)
        return "ok"

    def sensor_data(self):
        if self.periph:
            sensor_data = {
                'time' : str(datetime.datetime.now()),
                'temperature': self.periph.read_temperature(),
                'battery': self.periph.read_battery(),
            }
            return json.dumps(sensor_data)
        else:
            #return "{}"
            return '{"temperature":[1,2,3,4]}'

if __name__ == "__main__":
    server = Server()
    print server.scan()

    app = Flask(__name__)

    @app.route('/')
    def index():
        with open("html/index.html", "r") as f:
            return f.read()
        
    @app.route('/scan')
    def scan():
        return server.scan()

    @app.route('/scan_result')
    def scan_result():
        return server.scan_result()

    @app.route('/connect')
    def connect():
        return server.connect()

    @app.route('/sensor_data')
    def sensor_data():
        return server.sensor_data()

    app.run(debug=False, host="0.0.0.0")
