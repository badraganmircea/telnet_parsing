from telnet_connect import TelnetConnect
import response_parser

tn = TelnetConnect("route-views.routeviews.org")
tn.login("rviews", "")
print response_parser.contains(tn.get_response("show ip route 192.0.2.1"))
tn.exit()
