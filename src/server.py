import socket
import json

SECRET_KEY = '1234'


def broadcast(command, payload):
    data = json.dumps(
        {
            'secret_key': SECRET_KEY,
            'command': command,
            'payload': payload
        }
    )

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.sendto(bytes(data, encoding='utf-8'), (UDP_IP, UDP_PORT))
    print(f'message sent to {UDP_IP}:{UDP_PORT}')


if __name__ == '__main__':
    broadcast(
        command='CLOSE',
        payload={"test":1}
    )
