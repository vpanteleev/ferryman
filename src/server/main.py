import argparse
import socket

MAX_BYTES = 65535


def server(host, port):
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    main_socket.bind((host, port))

    print('Listen at {}:{}'.format(host, port))

    while True:
        data, client_address = main_socket.recvfrom(MAX_BYTES)
        print('Received message: {}, from {}'.format(data, client_address))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Client of Network application for transfer black matter")
    parser.add_argument('--host', default='127.0.0.1', help='what interface to use')
    parser.add_argument('--port', type=int, default=1060, help='what port to use')

    args = parser.parse_args()
    server(args.host, args.port)