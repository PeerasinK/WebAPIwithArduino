from flask import Flask, render_template
import serial, struct

app = Flask(__name__)

@app.route('/')
def index():
    return 'Arduino Test<br>Input: [1101, 2201]'

@app.route('/trigger/<id>')
def trigger(id):
    arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
    arduinoSerialData.write(struct.pack('>H', int(id)))
    return id + ' triggered'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')