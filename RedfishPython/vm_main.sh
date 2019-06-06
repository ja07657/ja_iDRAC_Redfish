#!/bin/sh
cat ipfile
echo "ok ? , if not, then break out"
read x
echo "Enter user for iDRAC"
read -s DRACUSER
echo "Enter password for iDRAC"
read -s DRACPASS
#
for DRACIP in `cat ipfile`
do
	echo "Running on..."$DRACIP
	#python $1 -ip $DRACIP -u $DRACUSER -p $DRACPASS
	python InstallFromRepositoryREDFISH.py -g y -ip $DRACIP -u $DRACUSER -p $DRACPASS ## get firmware inventory ##
 	python InsertEjectVirtualMediaREDFISH.py -o2 -d1 -ip $DRACIP -u $DRACUSER -p $DRACPASS ##eject##
 	python InsertEjectVirtualMediaREDFISH.py -o1 -d1 -i http://10.40.196.209/iso/Polaris_14G_June2019.iso -ip $DRACIP -u $DRACUSER -p $DRACPASS ##mount##
 	python InsertEjectVirtualMediaREDFISH.py -cy -ip $DRACIP -u $DRACUSER -p $DRACPASS ##status##
 	python SetNextOneTimeBootVirtualMediaDeviceOemREDFISH.py -d1 -ry -ip $DRACIP -u $DRACUSER -p $DRACPASS ## set onetime boot device to vm  and reboot y##

done
