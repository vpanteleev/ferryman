import argparse
import socket
import time


def client(host, port):
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    main_socket.sendto(str(time.time()).encode(), (host, port))
    print('Timestamp sent to {}:{}'.format(host, port))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Server of Network application for transfer black matter")
    parser.add_argument('--host', default='127.0.0.1', help='host of server')
    parser.add_argument('--port', type=int, default=1060, help='port of server')

    args = parser.parse_args()
    client(args.host, args.port)
