# coding=utf-8
# execute a simple command
from subprocess import Popen, PIPE
import getpass

shortshell_debug = False


def exe(run_cmd, show_error=False):
    user = getpass.getuser()
    home = "/home/" + user + "/"
    run_cmd = run_cmd.replace("~", home)
    if shortshell_debug:
        print("shortShell: " + run_cmd)
    if show_error:
        return Popen(run_cmd.split(), stderr=PIPE, stdout=PIPE).communicate()[0]
    else:
        return Popen(run_cmd.split(), stderr=PIPE, stdout=PIPE).communicate()[0]


# execute a command with dir
def exe_with_cwd(run_cmd, cwd_dir, show_error=False):
    if shortshell_debug:
        print("shortShell: " + run_cmd)
    if show_error:
        return Popen(run_cmd.split(), stderr=PIPE, stdout=PIPE, cwd=cwd_dir).communicate()
    else:
        return Popen(run_cmd.split(), stderr=PIPE, stdout=PIPE, cwd=cwd_dir).communicate()[0]


def adb_exe(new_cmd, show_error=False):
    new_cmd = "adb shell " + new_cmd
    return exe(new_cmd, show_error)


# execute a command with su
def adb_su_exe(run_cmd, show_error=False):
    new_cmd = 'adb shell su -c "' + run_cmd.replace("\"", "'") + '"'
    return exe(new_cmd, show_error)


def adb_exe_with_cwd(run_cmd, cwd_dir, show_error=False):
    new_cmd = "adb shell " + run_cmd
    if show_error:
        return Popen(new_cmd.split(), stderr=PIPE, stdout=PIPE, cwd=cwd_dir).communicate()
    else:
        return Popen(new_cmd.split(), stderr=PIPE, stdout=PIPE, cwd=cwd_dir).communicate()[0]

if __name__ == '__main__':
    out = exe("")