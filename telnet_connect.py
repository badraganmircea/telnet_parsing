import telnetlib
import ntplib
import time


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
        # print self.ntp.request(host, 2, 123, 5)
        print "Ntp server time", time.ctime(self.ntp.request(self.host, 2, 123, 5).tx_time)
