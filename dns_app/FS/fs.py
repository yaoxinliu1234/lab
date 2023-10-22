from flask import Flask, request, jsonify
import socket

app = Flask(__server__)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')

    if None in (hostname, ip, as_ip, as_port):
        return jsonify({"error": "Missing data in the request"}), 400

    msg = f'TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10'
    sock.sendto(msg.encode('utf-8'), (as_ip, int(as_port)))
    data, addr = sock.recvfrom(1024)
    if data.decode('utf-8') == 'OK':
        return 'Success', 201
    return 'Failure', 400

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if number is None:
        return jsonify({"error": "Lack of Parameter"}), 400
    try:
        number = int(number)
        if number < 0:
            return jsonify({"error": "Negative number not allowed"}), 400
        result = fib_helper(number)
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"error": "Bad Format"}), 400

def fib_helper(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    return fib_helper(x - 1) + fib_helper(x - 2)

if __name__ == '__main__':
    sock.bind(('127.0.1.1', 0))
    app.run(port=9090)

