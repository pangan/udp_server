import socket


def broadcast(message):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.sendto(message, (UDP_IP, UDP_PORT))
    print(f'message sent to {UDP_IP}:{UDP_PORT}')


if __name__ == '__main__':
    broadcast(b'hello')
