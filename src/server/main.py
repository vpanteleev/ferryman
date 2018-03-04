import argparse
import socket
from threading import Thread

MAX_BYTES = 65535


def tcp_server(host, port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # it's possible that some data have no been delivered yet,
    # or something, so we wait as a cautionous TCP implementation "

    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_socket.bind((host, port))
    tcp_socket.listen(1)

    print('TCP server listen at {}:{}'.format(host, port))

    while True:
        client_socket, socketname = tcp_socket.accept()
        print('TCP: Connection accepted -- {}'.format(socketname))

        data = client_socket.recvfrom(MAX_BYTES)
        print('TCP: Data -- {}'.format(data))
        client_socket.close()


def udp_server(host, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))

    print('UDP server listen at {}:{}'.format(host, port))

    while True:
        data, client_address = udp_socket.recvfrom(MAX_BYTES)
        print('UDP: Received message: {}, from {}'.format(data, client_address))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Client of Network application for transfer black matter")
    parser.add_argument('--host', default='127.0.0.1', help='what interface to use')
    parser.add_argument('--port', type=int, default=1060, help='what port to use')

    args = parser.parse_args()

    Thread(target=tcp_server, args=(args.host, args.port)).start()
    Thread(target=udp_server, args=(args.host, args.port)).start()