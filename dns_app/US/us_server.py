from flask import Flask, request, jsonify
import socket
app = Flask('user')
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        return 'error', 400
      print ("findig ip')

    try:
        fs_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        return jsonify({'error': 'DNS Resolution Failed'}), 400

    return jsonify({'fibonacci': fibonacci_result}), 200

if __name__ == '__main__':
    app.run(host='127.9.0.1', port=8080)
