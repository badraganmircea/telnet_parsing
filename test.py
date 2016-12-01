from telnet_connect import TelnetConnect

tn = TelnetConnect("route-views.routeviews.org")
tn.login("rviews", "")
tn.get_response("show ip route 192.0.2.1")
tn.exit()
