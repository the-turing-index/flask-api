from flask import Flask, jsonify
from data.calendars import calendars

app = Flask(__name__)

@app.route('/calendars')
def index():
    return jsonify(calendars)

if __name__ == '__main__':
    app.run()
