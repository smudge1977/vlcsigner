#
# Regular cron jobs for the vplayer package
#
0 4	* * *	root	[ -x /usr/bin/vplayer_maintenance ] && /usr/bin/vplayer_maintenance
