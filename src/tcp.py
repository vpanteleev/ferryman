import socket
from threading import Thread

MAX_BYTES = 65535

def dispatcher(host, port, pi):
    dispatcher_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # it's possible that some data have no been delivered yet,
    # or something, so we wait as a cautionous TCP implementation "

    dispatcher_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    dispatcher_socket.bind((host, port))
    dispatcher_socket.listen(1)

    print('Dispatcher listen at {}:{}'.format(host, port))

    while True:
        client_socket, socketname = dispatcher_socket.accept()
        print('Dispatcher: Connection accepted -- {}'.format(socketname))

        adapter = TCP_adapter(client_socket)
        Thread(target=pi, args=(adapter,)).start()


class TCP_adapter:
    def __init__(self, client_socket):
        self.socket = client_socket

    def read(self):
        raw_data, _ =  self.socket.recvfrom(MAX_BYTES)
        return raw_data.decode('ascii')

    def send(self, message):
        return self.socket.sendall(message.encode('ascii'))

    def close(self):
        return self.socket.close()