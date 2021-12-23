from flask import Flask, send_from_directory
import database
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return static_page('index.html')


@app.route('/static/<filename>')
def static_page(filename):
    return send_from_directory('static', filename)


@app.route('/api/get_random_meme')
def get_random_meme():
    return json.dumps(database.get_random())


@app.route('/api/like/<int:id>')
def like(id):
    return str(database.add_like(id))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
