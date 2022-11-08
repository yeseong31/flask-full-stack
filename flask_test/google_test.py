import requests
from flask import Flask

app = Flask(__name__)

host = '127.0.0.1'
port = 5000
url = 'https://www.google.co.kr'


@app.route('/google')
def get_google():
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    app.run(host=host, port=port)
