import subprocess
import os

import pycrest


def sound_alarm():
    with open(os.devnull, "wb") as f:
        subprocess.call(['/bin/sh', '-c', 'aplay warning_sound.wav'], stdout=f, stderr=f)


def main():
    eve = pycrest.EVE()
    eve()

    print eve.motd

    sound_alarm()


if __name__ == '__main__':
    main()
