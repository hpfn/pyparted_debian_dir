#!/usr/bin/python
# list primary partitions for a given device
import parted

device = parted.getDevice("/dev/sda")
disk = parted.Disk(device)


# obj.getLogicalPartitions() for logical
# obj.getExtendedPartition() for extended
primary_partitions = disk.getPrimaryPartitions();

for partition in primary_partitions:
	print "Partition: %s" % partition.path
	print "Size: %s Bytes" % partition.getSize(unit="b")
	try:
		fs = parted.probeFileSystem(partition.geometry)
	except:
		fs = "unknown"
	print "Filesystem: %s" % fs
	print "Start: %s End: %s" % (partition.geometry.start,partition.geometry.end)
