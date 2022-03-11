#coding:utf-8

import socket
import json
import requests
import flask
import re

app = flask.Flask(__name__)

@app.route("/")
def index_page():
        return flask.Response(json.dumps({"information":{"api_version":"1.0",
                "api_name":"internal_server", "object":{"type":"object", "permenant":"false"}}}), 200, mimetype="application/json")

@app.route("/api/v1/internal_server", methods=["GET"])
def internal_server():
        if(flask.request.method == "GET"):
                response_output = json.dumps({"error":"miss some arguments like 'host:port' and 'data'."})
                if(flask.request.args.get('host') and flask.request.args.get('data')):

                        internal_host_port = re.findall('([0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\:[0-9]{0,})', flask.request.args.get('host'))
                        address_ip, address_port = internal_host_port[0].split(":")

                        try:

                                socket_create      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                socket_create.connect((address_ip, int(address_port)))
                                socket_create.send(flask.request.args.get('data').encode())

                        except ConnectionRefusedError as exception_error_input:
                                return flask.Response(json.dumps({"error":"port not open."}), 200, mimetype="application/json")

                        return socket_create.recv(4096).decode()

                return flask.Response(response_output, 200, mimetype="application/json")

if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
