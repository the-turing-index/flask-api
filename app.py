from flask import Flask, jsonify
from flask_cors import CORS
from data.calendar_list import calendar_list

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/calendars')
def index():
    return jsonify(calendar_list)

if __name__ == '__main__':
    app.run()
