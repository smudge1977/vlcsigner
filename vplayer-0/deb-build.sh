#!/bin/bash

# Create folder with dh_make --native
#

# Could assert this from the control file?
PACKAGE_NAME=vplayer

# make vplayer.install ./source ./destination list of files to go in package


dpkg-buildpackage --no-sign

#dpkg-buildpackage -b -uc