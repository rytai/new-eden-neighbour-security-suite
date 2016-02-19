import subprocess
import os
import platform  # To find out whether we're on window, or linux
import urllib2
import urllib

import pycrest  # Api to connect to Crest

import requests
import json  # For parsing the received crest data.

linux_or_windows = platform.system()

if linux_or_windows != 'Linux' and linux_or_windows != 'Windows':
    print '''This script can only be run with linux or windows system.'
          Your system is: {}.'''.format(linux_or_windows)
    exit()


# Multi-platfrom warning sound when needed.
def sound_alarm():
    if linux_or_windows == 'Linux':
        with open(os.devnull, "wb") as f:
            subprocess.call(['/bin/sh', '-c', 'aplay warning_sound.wav'], stdout=f, stderr=f)

def getByAttrVal(objlist, attr, val):
    ''' Searches list of dicts for a dict with dict[attr] == val '''
    matches = [getattr(obj, attr) == val for obj in objlist]
    index = matches.index(True)  # find first match, raise ValueError if not found
    return objlist[index]


def main():
    eve = pycrest.EVE()
    eve()

    print 'Jita by name'+str(getByAttrVal(eve.systems().items, 'name', 'Jita'))

    jita = getByAttrVal(eve.systems().items, 'id', 30000142)

    print 'Jita info:'
    for line in str(jita()).split(','):
        print line

    #sound_alarm()


if __name__ == '__main__':
    main()
