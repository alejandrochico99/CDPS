#addwebhost.py
#Introducimos los dominios

import sys
from subprocess import call
import argparse
parser = argparse.ArgumentParser(description='Process domains')
parser.add_argument("-d",'--domain', metavar='', help='new domain')
args= parser.parse_args()
dominio = args.domain
def main():
	call("sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/%s.conf"%(dominio), shell = True)
	f = open ("/etc/apache2/sites-available/%s.conf"%(dominio), "r")
	lines = f.readlines()
	f.close()
	#f = open ('/etc/apache2/sites-available/000-default.conf')
	f = open ("/etc/apache2/sites-available/%s.conf"%(dominio),"w")

	for line in lines :
	    fields = line.strip().split()     # Array indices start at 0 unlike AWK 
	    if(len(fields) > 0):
	        if( fields[0] == "DocumentRoot"):
	            f.write("\nServerName "+dominio+"\nServerAlias www."+dominio+".cdps\n")
	    f.write(line)
	f.close()

	call("sudo a2ensite "+dominio+".conf", shell=True)
	call("sudo service apache2 reload", shell=True)
if __name__ == "__main__":
    main()
    



