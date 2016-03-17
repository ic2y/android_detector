# coding=utf-8
# execute a shell command,can save current path,support save and update system environment variables

from subprocess import check_output
import os
import sys
import getpass


class LongShell:

    m_user_name = None
    m_Home = None
    m_Path = None
    m_fout = sys.stdout
    m_fin = sys.stdin
    m_ferr = sys.stderr
    longshell_debug = True

    def __init__(self):
        self.m_user_name = getpass.getuser()
        self.m_Home = '/home/'+self.m_user_name
        self.m_Path = os.environ['PATH'].split(os.pathsep)

    def parse_cmd(self, run_cmd):
        args = run_cmd.split()
        args = [x.replace('~', self.m_Home) if ('~' in x) else x for x in args]
        if "cd" in args[0]:
            path = args[1]
            if os.path.exists(path):
                os.chdir(path)
            else:
                print('cd path errror.')
            return None
        elif "export" in args[0]:
            arr = args[1].split("=")
            if len(arr) == 2:
                if len(arr[1]) > 2:
                    if arr[1][0] == "'" and arr[1][-1] == "'":
                        arr[1] = arr[1][1:len(arr[1])-1]
                    elif arr[1][0] == '"' and arr[1][-1] == '"':
                        arr[1] = arr[1][1:len(arr[1])-1]
                    os.environ[arr[0]] = arr[1]
            return None
        else:
            return args

    def exe(self, run_cmd):
        if self.longshell_debug:
            print("longShell: "+run_cmd)
        try:
            if not run_cmd:
                return "error empty"
            args = self.parse_cmd(run_cmd)
            if args:
                if 'echo' in args[0]:
                    key = args[1][1:]
                    if key in os.environ:
                        return os.environ[key]
                    else:
                        return "echo error"
                if '&' in args:
                    try:
                        pid = os.fork()

                    except OSError, e:
                        print 'failed to fork '
                        sys.exit(1)
                    if pid == 0:
                        print 'forking success...'
                        args.remove(args[-1])
                        return check_output(args, stdin=self.m_fin, stderr=self.m_ferr)

                # normal execution
                else:
                    return check_output(args, stdin=self.m_fin, stderr=self.m_ferr)
            return "error longshell.exe"
        except Exception as e:
            return str(e)

'''
if __name__ == "__main__":
    cmd = "./aosp.sh /home/ic2y/code/android/WORKING_DIRECTORY /home/ic2y/aosp/out/arm-6.0 build/" \
          "envsetup.sh aosp_arm-eng external/cve_2014-9028_flac/"
    shell = LongShell()
    shell.exe("cd ../shell/")
    rs = shell.exe(cmd)
    print(rs)
'''