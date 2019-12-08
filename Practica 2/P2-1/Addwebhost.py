#!/usr/bin/python 



import sys
from subprocess import call
import os



#/etc/hosts

#192.168.122.241 dominio1   www.dominio1.cdps
#192.168.122.241 dominio2   www.dominio2.cdps

call(["sudo", "mkdir", "/home/pegaso/Documentos/cuarto/CDPS/var"])
call(["sudo", "mkdir", "/home/pegaso/Documentos/cuarto/CDPS/var/www"])
call(["sudo", "mkdir", "/home/pegaso/Documentos/cuarto/CDPS/var/www/dom1"])
call(["sudo", "mkdir", "/home/pegaso/Documentos/cuarto/CDPS/var/www/dom2"])