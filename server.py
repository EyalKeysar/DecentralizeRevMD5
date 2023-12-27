import socket
import threading
from task_handler import TaskHandler
from ServerAPI.protoconst import *
from ServerAPI.core_proto import *
class Server():
    def __init__(self, hashed_val):
        self.found = False
        self.hashed_val = hashed_val
        self.task_handler = TaskHandler()
        self.clients_list = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(1)

    def run(self):
        accept_thread = threading.Thread(target=self.accept_clients_thread)
        accept_thread.start()

    def accept_clients_thread(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print('Client connected: ', client_address)
            self.clients_list.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client_thread, args=(client_socket,))
            client_thread.start()


    def handle_client_thread(self, client):
        while True:
            if self.found:
                send_by_size(client, STOP)
                return
            try:
                data, command, params = recv_by_size(client)
                if command == HELLO:
                    send_by_size(client, HELLO)

                elif command == GETTASK:
                    start, end = self.task_handler.add_task_client(client)
                    print('Sending task: ', start, end)
                    send_by_size(client, TASKOK, str(start) + ',' + str(end) + ',' + self.hashed_val)

                elif command == FOUND:
                    print('Found: ', params)
                    send_by_size(client, FOUNDOK)
                    self.found = True

                elif command == NOTFOUND:
                    self.task_handler.task_checked(client, int(params.split(',')[0]), int(params.split(',')[1]))
                    send_by_size(client, NOTFOUNDOK)

            except:
                pass
        


if __name__ == '__main__':
    sServer = Server("e807f1fcf82d132f9bb018ca6738a19f")
    sServer.run()
