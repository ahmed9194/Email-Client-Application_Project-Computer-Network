import socket
from config import *

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TCP_HOST, TCP_PORT))

    while True:
        data = client.recv(1024)
        if data:
            print("Notification:", data.decode())

if __name__ == "__main__":
    start_client()
