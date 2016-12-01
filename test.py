from services import TelnetConnect, NtpConnect, MailService

tn = TelnetConnect("route-views.routeviews.org")
tn.login("rviews", "")
tn_res = tn.get_response("show ip route 192.0.2.1")
print "tn res is "+tn_res
tn.exit()

ntp = NtpConnect("2.ro.pool.ntp.org")
ntp_res = ntp.get_response()
print ntp_res

ms = MailService("badraganmircea", "")
ms.send_email(tn_res+"\n"+ntp_res)
