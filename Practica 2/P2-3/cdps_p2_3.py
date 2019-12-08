import libvirt
conn = libvirt.open("qemu:///system")

for id in conn.listDomainsID():
	dom = conn.lookupByID(id)
	infos = dom.info()
	print 'Nombre =  %s' % dom.name()
	print 'ID = %d' % id
	print 'Estado = %d' % infos[0]
	print 'Numero de maquinas virtuales = %d' % infos[3]
	print ' '