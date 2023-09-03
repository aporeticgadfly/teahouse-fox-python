teahouse-background-fox
=======================

A simple automated background switcher for gnome, to display the teahouse fox's adventures throughout the day

history
-------
Teahouse Fox was an iGoogle theme that showed us the idyllic life of a Fox.  He fed ducks, ate lunch, and he lit paper lamps at night. His simple joy, nestled in the background of a news feed, made my days a little brighter.

But then, in 2013, iGoogle was discontinued and the Teahouse Fox no longer had a home.

I imagine he has since been wandering the wastelands of the internet, seeking shelter and a return to his rustic peace, somehow maintaining his serene countenance despite the horrors he faced out in those wild dark places.

Homeless and wandering, until now.

Today his home has been reclaimed and reconstructed, painstakingly transported (grassblade by grassblade) onto my laptop’s wallpaper, thanks to the magic of bash, GNOME, and cron.

installation
------------

1.	Download this script to any suitable location (perhaps ~/bin or /.opt)
	- note: You can use "git clone" or you can manually download each file

2.	Add the appropriate entries to your cron schedule, setting script to run every hour at 0 minutes, passing the path to your python3 interpreter and the script location
   	- note: use crontab -e to edit your cron schedule
   	-example: 0 * * * * /usr/bin/python3 /path/to/script >> /path/to/your_script.log 2>&1

3.	Copy background-fox.desktop to ~/.config/autostart/. If this directory does not exist, create it.

4.	Edit ~/.config/autostart/background-fox.desktop to match script location
	- note: the only line that needs to be changed is line 5; set that to wherever you put the script.

5.	Logout and log back in, you should see the background updated to the appropriate fox!

changes from original version
------------
-changed from bash to python because who likes bash
-changed the timing of the picture changes slightly
-changed logging capability to include timestamps and other things
-fixed some bugs in the original
-credit to original: https://github.com/JoshuaD84/teahouse-fox-background

troubleshooting
------------
-ensure your desktop environment is GNOME
-check XDG_CURRENT_DESKTOP environment variable with echo $XDG_CURRENT_DESKTOP; output should say GNOME somewhere
-try running script manually to see if it will change from an empty background
-check steps outlined above for correctness
-ensure everything has the appropriate permissions
