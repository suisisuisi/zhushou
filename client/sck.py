# -*- coding: utf-8 -*-
#!/usr/local/bin/python3
import socket
class sck:
    server = ""
    def connect(self, server, port):
        try:
            self.server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.connect((server, port))
        except socket.error as e:
            print(e)

    def send(self,data):
        self.server.send(data)


    def heartbeat(self):
        # 心跳包机制

        pass
