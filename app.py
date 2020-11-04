from flask import Flask, jsonify
from flask_cors import CORS
from db.calendars import all_events, demo_all_events

app = Flask(__name__)
app.config.from_pyfile('config/settings.py')
CORS(app)

@app.route('/api/v1/calendars')
def index1():
    return jsonify(all_events)

@app.route('/api/v1/demo')
def index2():
    return jsonify(demo_all_events)
