

import telnetlib
import getpass

user = raw_input("Username: ")
password = getpass.getpass()

dev_list = ["192.168.1.2", "192.168.1.3", "192.168.1.4"]

for host in dev_list:
    print("configuring " + host + "\n")
    tn = telnetlib.Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("vlan database" + "\n")
    for x in range(2,10):
        tn.write("vlan " + str(x) + " name " + "lantai" + str(x-1) + "\n")

    tn.write("end\n")
    tn.write("exit\n")
    print tn.read_until("end")

#switch 26xx
