import argparse
import socket
from threading import Thread
import json

MAX_BYTES = 65535


def dispatcher(host, port):
    dispatcher_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # it's possible that some data have no been delivered yet,
    # or something, so we wait as a cautionous TCP implementation "

    dispatcher_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    dispatcher_socket.bind((host, port))
    dispatcher_socket.listen(1)

    print('Dispatcer listen at {}:{}'.format(host, port))

    while True:
        client_socket, socketname = dispatcher_socket.accept()
        print('Dispatcher: Connection accepted -- {}'.format(socketname))

        Thread(target=commander, args=(client_socket,)).start()


def commander(client_socket):
    while client_socket.fileno() != -1:

        raw_data, _ = client_socket.recvfrom(MAX_BYTES)
        print('Commander: Data -- {}'.format(raw_data))

        parsed_data = parse_command(raw_data)
        command = parsed_data['command']
        commands[command](parsed_data, client_socket)


def close_connection(client_socket):
    client_socket.close()


def authorize(data, client_socket):
     user = data['login'] == 'admin' and data['password'] == 'admin'
     response = 'Kama Kama! Krasaychik!' if user else 'San\' xyu sosi.'

     client_socket.sendall(response.encode('ascii'));
     print('Commander: Response -- {}'.format(response))


def parse_command(raw_data):
    return json.loads(raw_data.decode('ascii'))


def echo(data, client_socket):
    client_socket.sendall(data.encode('ascii'));


def close_connection(_, client_socket):
    client_socket.close()


commands = {'authorize': authorize,
            "close_connection": close_connection,
            "echo": echo}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Client of Network application for transfer black matter")
    parser.add_argument('--host', default='127.0.0.1', help='what interface to use')
    parser.add_argument('--port', type=int, default=1060, help='what port to use')

    args = parser.parse_args()

    Thread(target=dispatcher, args=(args.host, args.port)).start()