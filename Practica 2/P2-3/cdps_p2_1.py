import libvirt
conn = libvirt.open("qemu:///system")

# Crear una maquina virtual
dom = virDomain_obj.create()

# Clonar una maquina virtual
