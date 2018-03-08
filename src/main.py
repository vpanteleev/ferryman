import argparse
from threading import Thread
from tcp import dispatcher
from bmtp import interpreter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Client of Network application for transfer black matter")
    parser.add_argument('--host', default='127.0.0.1', help='what interface to use')
    parser.add_argument('--port', type=int, default=1060, help='what port to use')

    args = parser.parse_args()

    Thread(target=dispatcher, args=(args.host, args.port, interpreter)).start()