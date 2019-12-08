from subprocess import call

call("mkdir /mnt/tmp/prueba2", shell = True)
call("cp /mnt/vnx/repo/cdps/cdps-vm-base-p1.img.bz2 /mnt/tmp/prueba2/.", shell = True)
call("bunzip2 /mnt/tmp/prueba2/cdps-vm-base-p1.img.bz2", shell = True)
call("HOME=/mnt/tmp sudo virt-manager", shell = True)
