import subprocess
import os
import platform  # To find out whether we're on window, or linux
import urllib2
import urllib

import pycrest  # Api to connect to Crest
import parse_sde

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


def find_solar_system_neighbours(jumps_dictionary, current_system):
    assert isinstance(jumps_dictionary, dict)
    assert isinstance(current_system, str)
    list_of_neighbour_ids = []
    try:
        list_of_neighbour_ids = jumps_dictionary[current_system]
    except KeyError, k_error:
        print k_error
    return list_of_neighbour_ids


def get_solar_system_by_id(eve, id):
    return getByAttrVal(eve.systems().items, 'id', int(id))


def main():
    eve = pycrest.EVE()
    eve()

    print 'Jita by name' + str(getByAttrVal(eve.systems().items, 'name', 'Jita'))

    jita = getByAttrVal(eve.systems().items, 'id', 30000142)

    #  print 'Jita info:'
    for line in str(jita()).split(','):
        #print line
        pass

    # Get dict containing all the possible jumps between systems.
    jumps_dictionary = parse_sde.parse_sde()  # Jita neighbours

    immediate_neighbours_ids = find_solar_system_neighbours(jumps_dictionary, '30000142')
    immediate_neighbours = []

    for solar_system_id in immediate_neighbours_ids:
        new_system = get_solar_system_by_id(eve, solar_system_id)
        immediate_neighbours.append(new_system)

    # Get ID's from one jump away. no duplicates
    one_jump_neighbour_ids = []
    for neighbour_id in immediate_neighbours_ids:
        for one_jump_neighbour_id in find_solar_system_neighbours(jumps_dictionary, neighbour_id):
            if one_jump_neighbour_id not in immediate_neighbours_ids:
                if one_jump_neighbour_id not in one_jump_neighbour_ids:
                    one_jump_neighbour_ids.append(one_jump_neighbour_id)

    # Get system names from the id's
    one_jump_neighbours = []
    for one_jump_neighbour_id in one_jump_neighbour_ids:
        new_system = get_solar_system_by_id(eve, one_jump_neighbour_id)
        one_jump_neighbours.append(new_system)

    print "Jita neighbours:--------------------------------------------"
    for system in immediate_neighbours:
        print system.name
    print "2 jumps from jita:------------------------------------------"
    for system in one_jump_neighbours:
        print system.name

        # sound_alarm()


if __name__ == '__main__':
    main()
