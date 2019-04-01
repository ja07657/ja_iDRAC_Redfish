#!/bin/sh
cat ipfile
echo "ok ? , if not, then break out"
read x
echo "Enter user for iDRAC"
read -s DRACUSER
echo "Enter password for iDRAC"
read -s DRACPASS
#echo "Enter name of python redfish script"
#read PYTHON
#
for DRACIP in `cat ipfile`
do
	echo $ip" "$PYTHON
	#python $PYTHON -ip $DRACIP -u $DRACUSER -p $DRACPASS
	python $1 -ip $DRACIP -u $DRACUSER -p $DRACPASS
done
