#coding:utf-8

import socket
import base64
import json
import os
import sys

create_socket = socket.socket()
create_socket.bind(("127.0.0.1", 52006))

create_socket.listen()
while(True):
        client_socket, client_address = create_socket.accept()
        while(True):
                try:
                        recv_data_connection = client_socket.recv(1024).decode()
                        parse_json_argument  = json.loads(base64.b64decode(recv_data_connection).decode().rstrip("\n\r"))
                        os.system(parse_json_argument["cmd"])
                        print(parse_json_argument)
                        break
                except:
                        print("an error")
