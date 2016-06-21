# coding: utf-8

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from Logger import *
from itertools import cycle
import traceback


class Mailer():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.alias = None
        self.content = None
        self.subject = None
        self.receiver = None
        self.server = self.config()

    def gmail_config(self):
        host = "smtp.gmail.com"
        port = 587
        return host, port

    def config(self):
        cfg = self.gmail_config()
        server = smtplib.SMTP(cfg[0], cfg[1])
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        return server

    def pack(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.alias
        msg['To'] = self.receiver
        msg.attach(MIMEText(self.content, 'html', 'utf-8'))
        return msg

    def send(self):
        try:
            msg = self.pack()
            self.server.sendmail(self.username, self.receiver, msg.as_string())
            logger.info('Your email was sent successfully to %s' % self.receiver)
        except:
            logger.error('Your email was sent failure to %s' % self.receiver)
            logger.error(self.username)
            logger.error(traceback.format_exc())


def setup(usernames, password):
    cycle_usernames = cycle(usernames)
    mailer = None
    username = cycle_usernames.next()
    try:
        mailer = Mailer(username, password)
        with open("mail.htm", 'r') as html_file:
            content = html_file.read().strip()
            mailer.content = content
        mailer.subject = u"Your Subject"
        mailer.alias = u"Your Alias"
    except:
        username = cycle_usernames.next()
        logger.error('Next username: %s' % username)

    return mailer


def main():
    usernames = ["xxx@gmail.com", "xxxx@gmail.com", "xxxx@gmail.com"]
    password = "xxxxxxxxxxxxxx"

    mailer = setup(usernames, password)

    f = open('mail_list.txt', 'r')
    users = f.readlines()
    count = 1
    for user in users:
        user = user.strip()
        if not user.startswith('#'):
            print count
            mailer.receiver = user
            mailer.send()
            count += 1


if __name__ == '__main__':
    main()
