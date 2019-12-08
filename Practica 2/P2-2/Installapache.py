from subprocess import call
import sys
import os
call("touch /etc/network/interfaces.tmp", shell = True)
call("sudo chmod 777 /etc/network/interfaces.tmp", shell = True)
f=open('/etc/network/interfaces')
n=open('/etc/network/interfaces.tmp', 'w')

for line in f:
    fields = line.strip().split()
    if len(fields) > 0 :
        if fields[0] == 'source':
            if fields[1] == "/etc/network/interfaces.d/*.cfg":
                n.write("auto eth0\niface eth0 inet static\naddress 192.168.122.241\n netmask 255.255.255.0\ngateway 192.168.122.1\ndns-nameservers 192.168.122.1\n")
                continue
    n.write(line)
f.close()
n.close()

os.remove("/etc/network/interfaces")
os.rename("/etc/network/interfaces.tmp", "/etc/network/interfaces")

call("sudo apt-get install apache2", shell = True)
call("sudo apt-get install lynx", shell = True)
call("sudo apt-get install wget", shell = True)
call("sudo apt-get install curl", shell = True)

call("reboot",shell=True)

