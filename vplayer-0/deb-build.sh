#!/bin/bash

# Create folder with dh_make --native -s -e keith@sneconsulting.co.uk
#

# Could assert this from the control file?
PACKAGE_NAME=vplayer

# make vplayer.install ./source ./destination list of files to go in package
find opt -type f | grep -v "\.in" |                                                             \
    sed -e "s#^\(opt/ivencs/.*\)#./\1  ./opt/ivencs#"                                           \
    >> "debian/${PACKAGE_NAME}.install"

find usr -type f | grep -v "\.in" |                                                             \
    sed -e "s#^\(opt/ivencs/.*\)#./\1  ./opt/ivencs#"                                           \
    >> "debian/${PACKAGE_NAME}.install"

find lib -type f | grep -v "\.in" |                                                             \
    sed -e "s#^\(opt/ivencs/.*\)#./\1  ./opt/ivencs#"                                           \
    >> "debian/${PACKAGE_NAME}.install"


dpkg-buildpackage --no-sign

#dpkg-buildpackage -b -uc