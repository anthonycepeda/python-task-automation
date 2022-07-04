from ast import Str
import smtplib
import os
from app.utils.logger import set_logger
from email.mime.text import MIMEText
from base64 import b64decode

LOGGER = set_logger(__name__)

"""
To get an application password, go to your gmail account settings
> Google Login > Applications passwords to generate one 
"""

sender_email = os.getenv("SENDER_EMAIL")
sender_password = b64decode(os.getenv("SENDER_PASSWORD")).decode("utf-8")


def connect():
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(sender_email, sender_password)
        LOGGER.info("connected to Gmail server")
        return True
    except ConnectionError as e:
        LOGGER.exception(str(e))
    except smtplib.SMTPAuthenticationError as e:
        LOGGER.exception(str(e))


def send_mail(content: dict):
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(sender_email, sender_password)
        LOGGER.info("connected to Gmail server")

        msg = MIMEText(content["message"])
        msg["Subject"] = content["subject"]
        msg["From"] = sender_email
        msg["To"] = content["receiver_email"]

        server.sendmail(
            from_addr=sender_email,
            to_addrs=content["receiver_email"],
            msg=msg.as_string(),
        )
        LOGGER.info("email sent to: %s", content["receiver_email"])
    except ConnectionError as e:
        LOGGER.exception(str(e))
    except smtplib.SMTPAuthenticationError as e:
        LOGGER.exception(str(e))
