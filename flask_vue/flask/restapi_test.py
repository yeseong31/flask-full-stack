from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'GET':
        user = request.args.get('email')
        print(user)
    if request.method == 'POST':
        data = request.get_json()  # POST에서는 get_json() 함수를 이용하여 데이터를 가져옴
        print(data)
        print(data['email'])
    if request.method == 'PUT':
        user = request.args.get('email')
        print(user)
    if request.method == 'DELETE':
        user = request.args.get('email')
        print(user)

    return make_response(jsonify({'status': True}), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8082)
