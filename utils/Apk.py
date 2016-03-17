# coding=utf-8
# 负责各种检查工作
import time
import os
import ShortShell


# start a activity,and send some data
def am_start_activity(apk_name, send_data=""):
    counter = 0
    max_try_num = 20
    name_arr = apk_name.split(".")
    package_name = ".".join(name_arr[0:-2])
    package_and_activity_name = ".".join(name_arr[0:-1])

    do_am_start_activity(package_name, package_and_activity_name, send_data)
    while package_name not in ShortShell.exe("adb shell ps | grep "+package_name) and counter < max_try_num:
        counter += 1
        time.sleep(2)
        do_am_start_activity(package_name, package_and_activity_name, send_data)


# apk_call_name 's format com.meizu.music.MainAvtivity.apk
def do_am_start_activity(package_name, package_and_activity_name, send_data=""):
    cmd = "adb shell am start -n %s/%s" % (package_name, package_and_activity_name)
    if send_data != "":
        cmd += " -d " + send_data
    print(cmd)
    ShortShell.exe(cmd)


def install_apk(apk_path):
    counter = 0
    max_try_num = 20

    name_arr = os.path.basename(apk_path).split(".")
    package_name = ".".join(name_arr[0:-2])
    do_install_apk(apk_path)

    while package_name not in ShortShell.exe("adb shell pm -l | grep "+package_name) and counter < max_try_num:
        counter += 1
        time.sleep(2)
        do_install_apk(apk_path)


def do_install_apk(apk_path):
    ShortShell.exe("adb install -r " + apk_path)


def uninstall_apk(package_name):
    ShortShell.exe("adb uninstall " + package_name)


def kill_apk(package_name):
    ShortShell.exe("adb shell am force-stop " + package_name)