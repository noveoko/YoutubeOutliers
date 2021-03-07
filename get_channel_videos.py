from yt_videos_list import ListCreator


my_driver = 'firefox' # SUBSTITUTE DRIVER YOU WANT (options below)
lc = ListCreator(driver=my_driver, scroll_pause_time=0.8)


lc.create_list_for(url='https://www.youtube.com/user/schafer5')
lc.create_list_for(url='https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ', log_silently=True)
# Set `log_silently` to `True` to mute program logging to the console.
# The program will log the prgram status and any program information
# to only the log file for the channel being scraped
# (this is useful when scraping multiple channels at once with multi-threading).
# By default, the program logs to both the log file for the channel being scraped AND the console.


# see the new files that were just created:
import os
os.system('ls -lt | head')                      # MacOS/Linux
os.system('dir /O-D | find "_videos_list"')     # Windows

# for more information on using the module:
help(lc)