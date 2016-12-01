import telnetlib
import ntplib
import time
import smtplib
from email.mime.text import MIMEText


class TelnetConnect:
    def __init__(self, host):
        self.tn = self.__connect(host)

    def __connect(self, host):
        return telnetlib.Telnet(host)

    def login(self, user, password):
        self.tn.read_until("login: ", 5)
        self.tn.write(user + "\r\n")
        self.tn.read_until("Password: ", 5)
        self.tn.write(password + "\r\n")
        print self.tn.read_until(">", 10)

    def exit(self):
        self.tn.write("exit" + "\r\n")
        self.tn.close()

    def get_response(self, command):
        self.tn.write(command + "\r\n")
        return self.tn.read_until("free", 10)


class NtpConnect:
    def __init__(self, host):
        self.ntp = self.__connect()
        self.host = host

    def __connect(self):
        return ntplib.NTPClient()

    def get_response(self):
        return "Ntp server time "+time.ctime(self.ntp.request(self.host, 2, 123, 5).tx_time)


class MailService:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.smtp = self.__login(username, password)

    def __login(self, username, password):
        try:
            smtp = smtplib.SMTP('smtp.gmail.com:587')
            smtp.starttls()
            smtp.login(username, password)
            return smtp
        except(), e:
            print e

    def exit(self):
        self.smtp.quit()

    def send_email(self, message):
        try:
            self.smtp.sendmail(self.username + '@gmail.com', [self.username + '@gmail.com'], self.__message_format(message))
            print "Mesajul electronic a fost trimis cu succes"
        except(), e:
            print "Mesajul electronic nu a fost trimis cu succes"
            print e
        else:
            self.exit()

    def __message_format(self, message):
        msg = MIMEText(message)
        msg['Subject'] = 'some bull'
        msg['From'] = self.username + "@gmail.com"
        msg['To'] = self.username + "@gmail.com"
        return msg.as_string()
