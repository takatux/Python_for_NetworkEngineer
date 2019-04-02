

import telnetlib

import getpass

host = raw_input('Enter remote router IP Address: ')
user = raw_input('Enter remote router username: ')
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(raw_input('Enter username remote router: '))
if password:
    tn.read_until('Password: ')
    tn.write(getpass.getpass())

tn.write("conf t\n")
tn.write("int f0/0\n")
tn.write("ip add 192.168.2.1 255.255.255.0\n")
tn.write("no sh\n")
tn.write("exit\n")
tn.write("end\n")

print tn.read_all()

#reference Komarudin AR. otomatisasi jaringan dengan python
