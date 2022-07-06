from ast import Str
import smtplib
import os
from app.utils.logger import set_logger
from email.mime.text import MIMEText
from base64 import b64decode
from decouple import config

LOGGER = set_logger(__name__)

"""
To get an application password, go to your gmail account settings
> Google Login > Applications passwords to generate one 
"""


SENDER_EMAIL = config("SENDER_EMAIL")
SENDER_PASSWORD = config("SENDER_PASSWORD")

if SENDER_PASSWORD:
    SENDER_PASSWORD = b64decode(SENDER_PASSWORD).decode("utf-8")


def connect():
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
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
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        LOGGER.info("connected to Gmail server")

        msg = MIMEText(content["message"])
        msg["Subject"] = content["subject"]
        msg["From"] = SENDER_EMAIL
        msg["To"] = content["receiver_email"]

        server.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=content["receiver_email"],
            msg=msg.as_string(),
        )
        LOGGER.info("email sent to: %s", content["receiver_email"])
        return f"email sent to: {content['receiver_email']}"
    except ConnectionError as e:
        LOGGER.exception(str(e))
    except smtplib.SMTPAuthenticationError as e:
        LOGGER.exception(str(e))
