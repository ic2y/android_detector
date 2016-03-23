# coding=utf-8
__author__ = 'cyy'
from utils import Logger
from utils import Checker
import os
import argparse


def run_one_exp(exp_dir_path):
    if "py" not in exp_dir_path:
        exp_file_package = "exp."+exp_dir_path
        try:
            __import__(exp_file_package)
        except:
            print("load exp fail.."+exp_file_package)


# start scan cve folder
def detector_all_exp(folders):
    for folder in folders:
        if os.path.exists("exp/" + folder):
            exp_files_path = os.listdir("exp/" + folder)
            for exp_dir_path in exp_files_path:
                run_one_exp(folder+"."+exp_dir_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="detector for iscas nfs")
    parser.add_argument("--exp", action='store', dest='one_exp_dir',
                        default="",
                        help='just detector one detector')
    args = parser.parse_args()

    folders = ["cve"]

    Checker.upload_checker()

    if args.one_exp_dir:
        run_one_exp(args.one_exp_dir)
    else:
        detector_all_exp(folders)

    Logger.export_carsh_report()