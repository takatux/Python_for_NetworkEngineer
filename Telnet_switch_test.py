

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
for x in range(3,10):
    tn.write("vlan " + str(x) + " name " + "gedung" + str(x-2) + "\n")
tn.write("exit\n")
tn.write("end\n")

print tn.read_until("end")

#Using switch L3 26xx
