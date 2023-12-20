from core_proto import *
from protoconst import *
import socket
class ServerAPI:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        self.sock.connect((HOST, PORT))
        send_by_size(self.sock, HELLO)
        data = recv_by_size(self.sock)
        if(data != HELLO):
            raise Exception("Server did not respond with HELLO"
    
    def disconnect(self):
        self.sock.close()
    
    def get_task(self):
        send_by_size(self.sock, GETTASK)
        data, command, params = recv_by_size(self.sock)
        if(command == TASKOK):
            return (params.split(',')[0], params.split(',')[1], params.split(',')[2])
        else:
            raise Exception("Server responded with unknown command: " + command)
    
    def found(self, result):
        send_by_size(self.sock, FOUND, result)
        data, command, params = recv_by_size(self.sock)
        if(command == FOUNDOK):
            return
        else:
            raise Exception("Server responded with unknown command: " + command)
        
    
    def not_found(self):
        send_by_size(self.sock, NOTFOUND)
        data, command, params = recv_by_size(self.sock)
        if(command == NOTFOUNDOK):
            return
        else:
            raise Exception("Server responded with unknown command: " + command)