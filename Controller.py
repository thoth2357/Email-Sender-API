import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_transport(host: str, port: int, username: str, password: str):
    """creates smtp objects"""
    try:
        context = ssl.create_default_context()
        transport = smtplib.SMTP_SSL(host, port, context=context)
        transport.ehlo()
        transport.login(username, password)
        return transport
    except Exception:
        return None


def build_mail(From: str, To: str, Subject: str, Body: str):
    """Builds email to be sent"""

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = From
    message["To"] = To
    message["Subject"] = Subject

    # Add body to message
    message.attach(MIMEText(Body, "plain"))
    text = message.as_string()
    return text
