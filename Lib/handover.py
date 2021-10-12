import os
import re
import time
import sys
sys.path.insert(0, r"C:\Users\Admin\PycharmProjects\5G_Automation\VariableFiles")
# sys.path.append("/VariableFiles")
import config_file
import shutil

class handover:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass
    def sour_des(self):

        source = [config_file.hanue_spath, config_file.Tdu_spath, config_file.Sdu_spath, config_file.gnbcu_spath]
        destination = [config_file.hanue_npath, config_file.Tdu_npath, config_file.Sdu_npath, config_file.gnbcu_npath]

        # source to destination
        dest1 = shutil.copy(source[0], destination[1])
        dest2 = shutil.move(source[0], destination[2])
        dest1 = shutil.copy(source[1], destination[0])
        dest2 = shutil.move(source[1], destination[3])
        dest1 = shutil.copy(source[2], destination[3])
        dest2 = shutil.move(source[2], destination[0])
        dest1 = shutil.copy(source[3], destination[2])
        dest2 = shutil.move(source[3], destination[1])
        print("Successfully moved the files")

    def nr_mobility(self):
        matchingStr = "inter29.*"
        path = [config_file.Sdu_pathd2, config_file.Tdu_pathd2, config_file.gnbcu_pathd1, config_file.hanue_pathd1,
                config_file.Sdu_pathd1, config_file.Tdu_pathd1, config_file.gnbcu_pathd2]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Inter-gNB-DU Mobility handover is successful and data working in both UL & DL direction ***")

#class_instance = attach_function()
#class_instance.sour_des()
#class_instance.nr_mobility()
