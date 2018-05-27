from flask import Flask
import json
import datetime

ADDRESS = 'D4:81:CA:20:4E:8E'

from igrill import IGrillV2Peripheral

app = Flask(__name__)

if __name__ == "__main__":
    periph = IGrillV2Peripheral(ADDRESS)

    @app.route('/')
    def index():
        sensor_data = {
            'time' : str(datetime.datetime.now()),
            'temperature': periph.read_temperature(),
            'battery': periph.read_battery(),
        }
        return json.dumps(sensor_data)

    app.run(debug=False, host="0.0.0.0")
