import socket
from config import *
from plyer import notification

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TCP_HOST, TCP_PORT))

    while True:
        data = client.recv(1024)
        if data:
            message = data.decode()
            print("Notification:", message)

            notification.notify(
                title="Email Notification",
                message=message,
                timeout=5
            )

if __name__ == "__main__":
    start_client()
