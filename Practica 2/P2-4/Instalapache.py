#Instalapache.py
import sys
from subprocess import call
import os
 
#Abrimos la consola del servidor
#call("sudo -s",shell=True) //Necesario hacerlo manualmente
#Introducimos las propiedades
def main():
	n = open('/etc/network/interfaces',"r") 
	lines=n.readlines()
	n.close()
	f = open('/etc/network/interfaces',"w") 
	
	for line in lines :
	    fields = line.strip().split()     # Array indices start at 0 unlike AWK 
	    if(len(fields) > 0):
	        if(fields[0] == "source"):
	            if(fields[1] == "/etc/network/interfaces.d/*.cfg"):
	             	f.write("auto eth0\niface eth0 inet static\naddress 192.168.122.241\nnetmask 255.255.255.0\ngateway 192.168.122.1\ndns-nameservers 192.168.122.1\n")
			else:             	
	    		f.write(line)

	f.close()


	call("sudo apt-get install apache2", shell=True)
	call("sudo apt-get install lynx", shell=True)
	call("sudo apt-get install wget", shell=True )
	call("sudo apt-get install curl", shell=True )

	call("reboot", shell=True)
if __name__ == "__main__":
    main()

    



