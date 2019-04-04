

import telnetlib
import getpass

host = raw_input('Enter remote switch IP Address: ')
user = raw_input('Enter remote switch username: ')
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("vlan database\n")
tn.write("vlan 10 name student\n")
tn.write("vlan 20 name lecturer\n")
tn.write("exit\n")
tn.write("end\n")

print tn.read_until("end")

#Using switch L3 26xx
