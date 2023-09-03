#!/usr/bin/python

import os
from datetime import datetime

current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

def is_gnome_environment():
	desktop = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
	return 'gnome' in desktop

if is_gnome_environment():
	wallpaper_path = "~/Dokumente/Projects/Programming/teahouse-fox-background/imgs"
	expanded_wallpaper_folder = os.path.expanduser(wallpaper_path)
	current_datetime = datetime.now()
	current_hour = current_datetime.hour
	addendum = "/" + str(current_hour) + ".jpg"

	final_path = expanded_wallpaper_folder + addendum

	gsettings_scale_command = f"gsettings set org.gnome.desktop.background picture-options 'scaled'"
	gsettings_set_command = f"gsettings set org.gnome.desktop.background picture-uri 'file://{final_path}'"

	os.system(gsettings_scale_command)
	os.system(gsettings_set_command)
else:
	print(f"[{timestamp}] GNOME is not the active desktop environment. GNOME is required for this script to work.")

