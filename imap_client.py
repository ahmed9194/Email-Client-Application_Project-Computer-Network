import imaplib
import email
from config import *

def check_latest_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    if not email_ids:
        return None

    latest_id = email_ids[-1]
    status, data = mail.fetch(latest_id, "(RFC822)")

    msg = email.message_from_bytes(data[0][1])
    subject = msg["subject"]

    mail.logout()
    return subject