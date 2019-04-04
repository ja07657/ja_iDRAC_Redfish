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
	#python $PYTHON -ip $DRACIP -u $DRACUSER -p $DRACPASS
	python $1 -ip $DRACIP -u $DRACUSER -p $DRACPASS
done
