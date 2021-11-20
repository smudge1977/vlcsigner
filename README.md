# VPLAYER omxplayer

use omx to player different scenes at time of day

## PI User setup bits

Set wallpaper to black.png
```
pcmanfm --set-wallpaper yourfile.jpg
```


## systemd services



## vplayer 

Will be a script that launches 'scenes' these can then be called from starting systemd jobs and removed by stopping the job



# TODO etc

debian.control
Depends=omxplayer


crontab config 

gpu_mem setting


# How to get omxplay output logged in journal?


vlcsigner --play "/home/pi/git/vlcsigner/content/videoplayback.mp4"


https://unix.stackexchange.com/questions/397853/how-to-set-a-systemd-unit-to-start-after-loading-the-desktop


omxplayer  --no-keys --no-osd --loop --display 5 videoplayback.mp4


5 – On Raspberry Pi’s 1 – 3, the number 5 represents the display attached to the HDMI port on the device.

For the Pi 4, this value has been changed as there are now two HDMI ports.
4 – If you want the video player to output to the touchscreen display you will need to use the number 4.
2 – On a Raspberry Pi 4, the number 2 represents the display attached to the HDMI0 port.
7 – Only on a Pi 4, the number 7 will represent the display that has been attached to the HDMI1 port.


omxplayer --no-keys --loop --display 5 bigbuckbunny_30sclip.mp4
omxplayer --no-keys --no-osd --loop --display 5 videoplayback.mp4 --layer 1 --alpha 255 --win 200 200 500 500


omxplayer --no-keys --no-osd --loop --display 5 --layer 2 bigbuckbunny_30sclip.mp4




### Notes

openbox maybe the After or requires but all seems to start fine
