# this detector's core source code is come from android-vts

# start detector cve_2015_6616
from utils import Checker
from utils import Phone
from utils import Apk
from utils import Logger
def check():
    poc_name = "cve_2015_6616"
    apk_name = "com.example.ic2y.cve_2015_6616.MainActivity.apk"
    apk_path = "exp/cve/cve_2015_6616/poc/" +apk_name
    package_name = Apk.get_package_name(apk_name)

    print("---------start init "+poc_name+"---------")
    Phone.wait_phone_alive() #make sure phone ok
    Checker.phone_ready()   #set checker
    Apk.install_apk(apk_path)
    Apk.am_start_activity(apk_name)

    if Checker.is_apk_crash():
        Logger.log_to_report_crash(poc_name)

    Apk.uninstall_apk(package_name)
    print("uninstall " + package_name)
    print("---------end "+poc_name+"---------")
