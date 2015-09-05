#!/usr/bin/python
# simple example on how to list available devices on system
import parted

devices = parted.getAllDevices();

for device in devices:
    geom = device.hardwareGeometry;
    ssize = device.sectorSize;
    size = (geom[0] * geom[1] * geom[2] * ssize) / 1000 / 1000 / 1000;

    print "Model: %s" %   device.model
    print "Size: %s GB" %  size 
    print "Heads: %s" %  geom[0]
    print "Sectors: %s" %  geom[2]
    print "Sector Size: %s" % ssize; 
