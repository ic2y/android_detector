# coding=utf-8
# check mobile run's status ,check crash and other ..

import ShortShell
import time
TIME_OUT = 30
SLEEP_ONCE_TIME = 3
# set phone is ready to check vulnerability
def phone_ready():
        ShortShell.adb_exe("echo 'ready' > /data/local/tmp/done")


def get_phone_status():
        return ShortShell.adb_exe("cat /data/local/tmp/done")


def is_apk_crash():
        start = 0
        while start < TIME_OUT:
                if "ready" in get_phone_status():
                        start += SLEEP_ONCE_TIME
                        time.sleep(SLEEP_ONCE_TIME)
                else:
                        break
        return "apk_crash" in get_phone_status()


def upload_checker():
        ShortShell.exe("adb push tools/bin/check /data/local/tmp/")
        ShortShell.exe("adb shell chmod 777 /data/local/tmp/check")
