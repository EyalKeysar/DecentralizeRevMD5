import socket
import threading
from task_handler import TaskHandler
from ServerAPI.protoconst import *

def main():
    task_handler = TaskHandler()
    in_handle = []
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    while True:
        client_socket, address = server_socket.accept()
        
    
    
def handle_client():


if __name__ == '__main__':
    main()