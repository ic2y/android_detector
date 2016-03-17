# coding=utf-8
__author__ = 'cyy'
from utils import Logger
import os

if __name__ == "__main__":
    folders = ["cve"]
    # start scan cve folder
    for folder in folders:
        if os.path.exists("exp/" + folder):
            exp_files_path = os.listdir("exp/" + folder)
            for exp_file_path in exp_files_path:
                if "py" not in exp_file_path:
                    exp_file_package = "exp."+folder+"."+exp_file_path
                    __import__(exp_file_package)



    Logger.export_carsh_report()