import re

s = "Known via \"bgp 23434\""


def contains(string_to_check):
    return re.search("(Known via \"bgp (\d{1,5})\")", string_to_check).groups()[0]


# print s
# print contains(s)
