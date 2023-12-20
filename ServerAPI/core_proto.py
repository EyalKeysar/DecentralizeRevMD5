from protoconst import *

def send_by_size(sock, command, params=None):
    data = command + params
    size = len(data)
    packet = size + SIZE_DATA_SEP + data
    sock.sendall(packet.encode())
    return

def recv_by_size(sock):
    datalen = ''
    cur_char = ''
    while cur_char != SIZE_DATA_SEP:
        cur_char = sock.recv(1).decode()
        datalen += cur_char
    
    datalen = int(datalen[:-1])
    data = sock.recv(datalen).decode()
    command = data[:6]
    params = data[6:]
    return data, command, params