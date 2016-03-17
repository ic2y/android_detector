# coding=utf-8
import ShortShell


# get process infomation,return a dict.key is process's name,value is process's pid
def ps_2_dict():
    ps_cmd = "ps"
    d = {}
    output = ShortShell.adb_exe(ps_cmd)
    arr = output.split("\r\n")
    for line in arr:
        if "PID" in line or line == "":
            continue
        line_arr = line.split()
        line_arr_size = len(line_arr)
        d[line_arr[line_arr_size - 1]] = line_arr[1]
    return d


# diff two process dict
def diff_ps_dict(old_dict, new_dict):
    d = {}
    if len(old_dict) == 0 or len(new_dict) == 0:
        return d
    for key in old_dict:
        if key in new_dict and old_dict[key] == new_dict[key]:
            continue
        d[key] = old_dict[key]
    return d


# check is target_string process crash
def is_ps_crash(diff_dict, target_str):
    target_arr = target_str.split(",")
    if len(target_arr) == 0 or len(target_str) == 0:
        return False
    for key in diff_dict:
        for target in target_arr:
            if target in key:
                return True
    return False