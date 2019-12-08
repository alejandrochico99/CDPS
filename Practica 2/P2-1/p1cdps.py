#!/usr/bin/python 


"""Una vez hayamos accedido a la máquina, debemos modificar la dirección
de red de la 
máquina  virtual  editando  el  fichero 
/etc/network/interfaces. Hay  que  tener  en cuenta que la imagen de la máquina virtual sólo incluye el editor de textos vi. 

sudo vi /etc/network/interfaces

Sustituya la línea:

source /etc/network/interfaces.d/*.cfg

por:

auto eth0
iface eth0 inet static
address 192.168.122.241
netmask 255.255.255.0
gateway 192.168.122.1
dns - nameservers 192.168.122.1

Guarde los cambios y rearranque la máquina con el comando reboot.

sudo apt
-
get update
sudo apt
-
get install nano



sudo apt
-
get install apache2
sudo apt
-
get
install lynx
sudo apt
-
get install wget
sudo apt
-
get install curl


Nota: Para  la  realización  posterior  de  los  scripts  es  necesario  recordar  que  la 
ejecución  de  los  comandos  unix  retornan  el  resul
tado  de  la  operación  (si  ha 
concluido con éxito o no). Esto se podrá utilizar como condición dentro de un script.



/var/www/html

sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/dominio1.conf 

Justo debajo de la directiva 
DocumentRoot
debemos añadir las siguientes líneas:

ServerName dominio1.cdps
ServerAlias www.dominio1.cdps

3. 
Ahora es preciso indicar al servidor que la configuración que debe cargar es otra a 
la que se ins
taló por defecto. Para ello, cargamos la nueva configuración:

sudo a2ensite dominio1.conf


4. Finalment
e rearrancamos el servicio de A
p
ache para aplicar los cambio
s. 

service apache2 reload

Primero se deben crear los dos directorios que van a almacenar los c
ontenidos de 
cada uno de los dominios. Para ello basta ejecutar los comandos:

sudo mkdir /var/www/dom1
sudo mkdir /var/www/dom2

// Fichero index.html en dom1
<h
tml>
<h1> Primer servidor </h1>
</html>

Se puede,
no obstante, incluir todo el contenido que se desee. Se repite el proceso 
para el segundo dominio.



Uso de una librería de python que facilite la labor (solo en el caso de realizar la 
práctica en nuestro ordenador personal
por ser necesario ser superusuario en la 
máquina 
).
Existen diversas bibliotecas pero una reciente y muy flexible es K
vm 
(
http
s://pypi.python.org/pypi/kvm/1.0.4
) 
o 
MyKvm 
(
https://pypi.python.org/pypi/mykvm/0.3.8
)  e
sta  última  como  herramienta 
complementaria para
escenarios más complejos.

Nota
: 
para copiar ficheros del ordenador de trabajo a la máquina virtual  podremos 
usar el comando SCP.
(ejecutar el comando “man scp” para más información )

Mejora opcional : uso del sistema de permisos de unix 
para mejorar la s
eguridad de la solución.
Se diseñara una solución usando grupos y un usuario unix nuevo por 
cada sitio web. 
Hay que tener en cuenta que el servidor apache se ejecuta como el usuario WWW.







"""




import sys 

from subprocess import call

print ("Hola Mundo") # "Hola Mundo"
print ("hola", "mundo") # "hola mundo"
print ("Hola" + "Mundo") # "HolaMundo"

call(["ls", "-l"])

f = sys.stdin
# If you need to open a file instead:
f = open('/etc/network/interfaces')
for line in f:
	print(line.strip())
	# fields = line.strip().split()
	# Array indices start at 0 unlike AWK

#	if (len(fields) != 0):
#		for word in fields: