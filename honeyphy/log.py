from flask import Flask, request, jsonify
import argparse
import json

app = Flask(__name__)
meth = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
parser = argparse.ArgumentParser()
parser.add_argument("port")
args = parser.parse_args()

# @app.route('/', methods=['GET'])
# def get_logs():
#     try:
#         with open("webserver.log", "r") as file:
#             logs = file.readlines()
#         return '<pre>' + ''.join(logs) + '</pre>'
#     except FileNotFoundError:
#         return "There's no log"
    

# @app.route('/', methods=['GET'])
# def get_logs():
#     try:
#         with open("webserver.log", "r") as file:
#             logs = file.readlines()
#             logs = [json.loads(log.strip()) for log in logs]
#         return json.dumps(logs, indent=4)
#     except FileNotFoundError:
#         return "There's no log"

@app.route('/', methods=['GET'])
def get_logs():
    try:
        with open("webserver.log", "r") as file:
            logs = file.readlines()
            logs = [json.loads(log.strip()) for log in logs]
        return jsonify({"logs": logs})
    except FileNotFoundError:
        return jsonify({"message": "There's no log"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=args.port, debug=False)