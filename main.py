import subprocess
import os
import platform  # To find out whether we're on window, or linux
import urllib2
import urllib

import pycrest  # Api to connect to Crest

linux_or_windows = platform.system()

if linux_or_windows != 'Linux' and linux_or_windows != 'Windows':
    print '''This script can only be run with linux or windows system.'
          Your system is: {}.'''.format(linux_or_windows)


# Sound alaaarm!
def sound_alarm():
    if linux_or_windows == 'Linux':
        with open(os.devnull, "wb") as f:
            subprocess.call(['/bin/sh', '-c', 'aplay warning_sound.wav'], stdout=f, stderr=f)


def main():
    eve = pycrest.EVE()
    eve()

    print eve.motd
    print eve.regions
    # The Forge region ID is 10000002, from eve.regions
    urllib.urlretrieve("https://public-crest.eveonline.com/regions/10000002/", "temp_forgedata")
    data = urllib2.urlopen('https://public-crest.eveonline.com/regions/10000002/')
    print data.read()

    # Next up: https://docs.python.org/2/library/json.html


    sound_alarm()


if __name__ == '__main__':
    main()
