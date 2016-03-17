# coding=utf-8
# check mobile run's status ,check crash and other ..

import ShortShell

# set phone is ready to check vulnerability
def phone_ready():
        ShortShell.adb_exe("echo 'ready' > /data/local/tmp/done")

def get_phone_status():
        return ShortShell.adb_exe("cat /data/local/tmp/done")

def is_apk_crash():
        return "apk_crash" in get_phone_status()