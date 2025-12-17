import socket
from imap_client import check_latest_email
from config import *
import time

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCP_HOST, TCP_PORT))
    server.listen(1)

    print("Notification Server started...")

    conn, addr = server.accept()
    print("Client connected:", addr)

    last_subject = None

    while True:
        subject = check_latest_email()
        if subject and subject != last_subject:
            message = f"New Email Received: {subject}"
            conn.send(message.encode())
            last_subject = subject
        time.sleep(5)

if __name__ == "__main__":
    start_server()
