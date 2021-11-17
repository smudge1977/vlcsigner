# vlcsigner
Control VLC instances for signage type usages


## Setup 

to be done in a package eventually!

Turn off low power warning etc
'''
sudo vi /boot/config.txt
avoid_warnings=1
'''

sym link files in packaging to where they will end up!
#TODO: helper script to do this when working on packaging stuff?

## Screen blanking
[reference](https://pimylifeup.com/raspberry-pi-disable-screen-blanking/)

These commands do need to be run from teh X enviroment
'''
xset s noblank
xset -dpms
# xset -s off    does not seem to work
'''