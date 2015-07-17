import re

IP=raw_input("enter the IP address: ");
pat = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
i = pat.match(IP)
if i:
   print "valid ip address"
else:
   print "invalid ip address"


