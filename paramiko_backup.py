
import paramiko
import time
import getpass

iplist = ["192.168.1.2", "192.168.1.3", "192.168.1.4"]
username = raw_input("Username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for ipaddress in iplist:
    ssh_client.connect(hostname=ipaddress, username=username, password=password)

    print "Success Login to {0}".format(ipaddress)
    conn = ssh_client.invoke_shell()

    conn.send("terminal length 0\n")
    conn.send("sh run\n")
    time.sleep(4)

    output = conn.recv(65535)
    output_file = open("{0}.cfg".format(ipaddress),"w")
    output_file.write(output)
    output_file.close()

    print("Config saved as {0}.cfg".format(ipaddress))

ssh_client.close()
