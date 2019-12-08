from subprocess import call
import sys
import os

call("sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/dominio1.conf", shell=True)
call("touch /etc/apache2/sites-available/dominio1.conf.tmp" , shell=True)
call("sudo chmod 777 /etc/apache2/sites-available/dominio1.conf.tmp", shell=True)
fin = open("/etc/apache2/sites-available/dominio1.conf")
fout = open("/etc/apache2/sites-available/dominio1.conf.tmp","w")
for line in fin:
        fields = line.strip().split()
        if len(fields) > 0:
                if fields[0] == "DocumentRoot":
                        if fields[1] == "/var/www/html":
                                fout.write("DocumentRoot /var/www/"+sys.argv[1]+"\n")
                                fout.write("ServerName dominio1.cdps\nServerAlias www.dominio1.cdps\n")
                                continue
        fout.write(line)
fin.close()
fout.close()
os.remove("/etc/apache2/sites-available/dominio1.conf")
os.rename("/etc/apache2/sites-available/dominio1.conf.tmp","/etc/apache2/sites-available/dominio1.conf")
call("sudo a2ensite dominio1.conf", shell=True)
call("service apache2 reload", shell=True)
call("sudo mkdir /var/www/"+sys.argv[1], shell=True)
call("touch /var/www/"+sys.argv[1]+"/index.html.tmp", shell=True)
call("touch /var/www/"+sys.argv[1]+"/index.html", shell = True)
call("sudo chmod 777 /var/www/"+sys.argv[1]+"/index.html.tmp", shell = True)
findex = open("/var/www/"+sys.argv[1]+"/index.html")
foutdex = open("/var/www/"+sys.argv[1]+"/index.html.tmp","w")
lineas = "Hola"
foutdex.write(lineas)
findex.close()
foutdex.close()
os.remove("/var/www/"+sys.argv[1]+"/index.html")
os.rename("/var/www/"+sys.argv[1]+"/index.html.tmp","/var/www/"+sys.argv[1]+"/index.html")




