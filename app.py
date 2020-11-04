from flask import Flask, jsonify
from flask_cors import CORS
from db.calendars import all_events

app = Flask(__name__)
app.config.from_pyfile('config/settings.py')
CORS(app)

@app.route('/api/v1/calendars')
def index():
    return jsonify(all_events)
