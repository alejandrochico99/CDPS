import sys
from subprocess import call
import os
 
    
#Introducimos las propiedades

f = open('/home/pegaso/Documentos/cuarto/CDPS/interfaces') 
n = open("/home/pegaso/Documentos/cuarto/CDPS/a.tmp", "w")

for line in f:
    fields = line.strip().split()     # Array indices start at 0 unlike AWK 
    if(len(fields) > 0):
        
        if( fields[0] == "source"):
            if(fields[1] == "/etc/network/interfaces.d/*"):
                n.write("auto eth0\niface eth0 inet static\naddress 192.168.122.241\nnetmask 255.255.255.0\ngateway 192.168.122.1\ndns-nameservers 192.168.122.1\n")
                continue
    
    n.write(line)
    
f.close()
n.close()

os.remove("/home/pegaso/Documentos/cuarto/CDPS/interfaces")
os.rename("/home/pegaso/Documentos/cuarto/CDPS/a.tmp", "/home/pegaso/Documentos/cuarto/CDPS/interfaces")


call(["apt-get", "install", "apache2"])
call(["apt-get", "install", "lynx"])
call(["apt-get", "install", "wget"] )
call(["apt-get", "install", "curl"] )


"""
#Introducimos los dominios

f = open ('/etc/apache2/sites-available/000-default.conf')
n = open ('/etc/apache2/sites-available/dominio1.conf', "w")

for line in f:
    fields = line.strip().split()     # Array indices start at 0 unlike AWK 
    n.write(line)
    if(len(fields) > 0):

        if( fields[0] == "DocumentRoot"):
            n.write("\nServerName dominio1.cdps\nServerAlias www.dominio1.cdps\n")

f.close()
n.close()

call(["a2ensite","dominio1.conf"])
call(["service","apache2", "reload"])
    
"""
