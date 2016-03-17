# coding=utf-8
# control mobile phone
import sys
import time

import ShortShell

timeout = 90
wait_time_step = 3


# reboot phone,wait until phone reboot.
def wait_reboot_phone():
    ShortShell.exe("adb shell reboot")
    # some phone will not reboot immediately,wait some seconds
    # wait adb connection lose
    # wait adb connection reconnect
    counter = 0
    while counter < timeout:
        if "root" not in ShortShell.exe("adb shell ls"):
            break
        print("wait phone alive...")
        time.sleep(wait_time_step)
        counter += wait_time_step

    counter = 0
    while counter < timeout:
        print("wait phone alive...")
        if "root" in ShortShell.exe("adb shell ls"):
            break
        time.sleep(wait_time_step)
        counter += wait_time_step

    if counter < timeout:
        pass
    else:
        print("wait phone timeout...quit android_detector")
        sys.exit(-1)


def wait_phone_alive():
    counter = 0
    while counter < timeout:

        if "root" in ShortShell.exe("adb shell ls"):
            break
        print("wait phone alive...")
        time.sleep(wait_time_step)
        counter += wait_time_step

    if counter < timeout:
        pass
    else:
        print("wait phone timeout...quit android_detector")
        sys.exit(-1)

