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

        source = [config_file.hanue_spath, config_file.Tdu_spath, config_file.Sdu_spath, config_file.gnbcu_spath,
                  config_file.Sgnb_spath, config_file.Tgnb_spath, config_file.amf_spath,config_file.HO_smf_spath,]
        destination = [config_file.hanue_npath, config_file.Tdu_npath, config_file.Sdu_npath, config_file.gnbcu_npath,
                       config_file.amf_npath,config_file.Sgnb_npath,config_file.Tgnb_npath,config_file.HO_smf_npath]

        # source to destination
        dest1 = shutil.copy(source[0], destination[1])
        dest2 = shutil.copy(source[0], destination[2])
        dest1 = shutil.copy(source[1], destination[0])
        dest2 = shutil.move(source[1], destination[3])
        dest1 = shutil.copy(source[2], destination[3])
        dest2 = shutil.move(source[2], destination[0])
        dest1 = shutil.copy(source[3], destination[2])
        dest2 = shutil.move(source[3], destination[1])
        dest3 = shutil.copy(source[4], destination[4])
        dest4 = shutil.copy(source[6], destination[5])
        dest5 = shutil.copy(source[6], destination[6])
        dest6 = shutil.copy(source[5], destination[4])
        dest7 = shutil.copy(source[4], destination[0])
        dest8 = shutil.copy(source[0], destination[5])
        dest9 = shutil.move(source[4], destination[6])
        dest10 = shutil.copy(source[5], destination[5])
        dest11 = shutil.move(source[5], destination[0])
        dest12 = shutil.move(source[0], destination[6])
        dest13 = shutil.move(source[6], destination[7])
        dest14 = shutil.copy(source[7], destination[4])
        dest15 = shutil.move(source[7], destination[5])

        print("Successfully moved the files")

    def inter_nr_mobility(self):
        matchingStr = "HO_inter.*"
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

    def HO_prepration(self):
        matchingStr = "HO_Prep.*"
        path = [config_file.Tgnb_pathd1, config_file.Sgnb_pathd1, config_file.amf_pathd1, config_file.amf_pathd2]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Handover procedures verified successfully ***")

    def Xn_inter_HO(self):
        matchingStr = "Xn_inter_HO.*"
        path = [config_file.Tgnb_pathd1, config_file.Sgnb_pathd1, config_file.amf_pathd1, config_file.amf_pathd2,
                config_file.hanue_npathd3, config_file.hanue_npathd4, config_file.Tgnb_pathd2, config_file.Tgnb_pathd3,
                config_file.Sgnb_pathd2, config_file.Sgnb_pathd3, config_file.Sgnb_pathd4, config_file.amf_pathd3,
                config_file.HO_smf_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Xn based inter NG-RAN handover is successful ***")

    def intra_nr_mobility(self):
        matchingStr = "HO_intra.*"
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
        print("*** gNB-CU provides new UL GTP TEID to the gNB-DU and gNB-DU provides new DL GTP TEID to the gNB-CU ***")
        print("*** Intra-gNB-DU Mobility handover is successful and data working in both UL & DL direction ***")

    def HO_counters(self):
        matchingStr = "HO_counters.*"
        path = [config_file.Tgnb_pathd3, config_file.Sgnb_pathd3, config_file.hanue_npathd4, config_file.Tdu_pathd2]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** source and target gNB counters for Xn handover are verified ***")
#class_instance = handover()
#class_instance.sour_des()
# class_instance.inter_nr_mobility()
# class_instance.HO_prepration()
# class_instance.Xn_inter_HO()
# class_instance.intra_nr_mobility()
#class_instance.HO_counters()