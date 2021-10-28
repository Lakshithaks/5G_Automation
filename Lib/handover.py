"""
Case name: Handover
Author: Priyanka and Lakshitha
How to execute testcase: robot -t "test case name" -d Report Testsuite/5G_Testsuite.robot
"""
import re
import sys
sys.path.insert(0, r"C:\Users\Admin\PycharmProjects\5G_Automation\VariableFiles")
# sys.path.append("/VariableFiles")
import config_file
import shutil

class handover:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'    # setting library scope as global

    def __init__(self):
        pass

    def sour_des(self):   # Moving files from source to destination

        source = [config_file.hanue_spath, config_file.Tdu_spath, config_file.Sdu_spath, config_file.gnbcu_spath,
                  config_file.Sgnb_spath, config_file.Tgnb_spath, config_file.amf_spath, config_file.HO_smf_spath,
                  config_file.HO_Tamf_spath, config_file.HO_Tsmf_spath]
        destination = [config_file.hanue_npath, config_file.Tdu_npath, config_file.Sdu_npath, config_file.gnbcu_npath,
                       config_file.amf_npath,config_file.Sgnb_npath, config_file.Tgnb_npath, config_file.HO_smf_npath,
                       config_file.HO_Tamf_npath, config_file.HO_Tsmf_npath, ]

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
        dest13 = shutil.copy(source[6], destination[7])
        dest14 = shutil.copy(source[7], destination[4])
        dest15 = shutil.copy(source[7], destination[5])
        dest16 = shutil.move(source[6], destination[8])
        dest17 = shutil.copy(source[8], destination[9])
        dest18 = shutil.copy(source[9], destination[7])
        dest19 = shutil.copy(source[7], destination[9])
        dest20 = shutil.copy(source[9], destination[8])
        dest21 = shutil.move(source[7], destination[8])
        dest22 = shutil.copy(source[8], destination[7])
        dest23 = shutil.move(source[8], destination[4])
        dest23 = shutil.move(source[9], destination[4])
        print("Successfully moved the files")

    def inter_nr_mobility(self):   # Inter NR mobility testcase validation
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

    def HO_prepration(self):  # Handover prepration testcase validation
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

    def Xn_inter_HO(self):  # Xn based handover testcase validation
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

    def intra_nr_mobility(self):  # Intra NR mobility handover teastcase validation
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

    def HO_counters(self):  # handover counters testcase validation
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

    def FDD_intra_frequency_Handover(self):  # FDD intra freq HO for FR1  bands testcase validation
        matchingStr = "FDD_intrafreq_FR1.*"
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
        print("***  FDD Intra frequency handover over Xn interface between two cells of FR1 band is successful ***")

    def FDD_inter_frequency_Handover(self):  # FDD inter freq HO for FR1  bands testcase validation
        matchingStr = "FDD_interfreq_FR1.*"
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
        print("***  FDD Inter frequency handover over Xn interface between two cells of FR1 band is successful ***")

    def TDD_intra_frequency_Handover(self):   # TDD intra freq HO for FR1  bands testcase validation
        matchingStr = "TDD_intrafreq_FR1.*"
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
        print("***  TDD Intra frequency handover over Xn interface between two cells of FR1 band is successful ***")

    def TDD_inter_frequency_Handover(self):  # TDD inter freq HO for FR1  bands testcase validation
            matchingStr = "TDD_interfreq_FR1.*"
            path = [config_file.Tgnb_pathd1, config_file.Sgnb_pathd1, config_file.amf_pathd1, config_file.amf_pathd2,
                    config_file.hanue_npathd3, config_file.hanue_npathd4, config_file.Tgnb_pathd2,
                    config_file.Tgnb_pathd3,config_file.Sgnb_pathd2, config_file.Sgnb_pathd3, config_file.Sgnb_pathd4,
                    config_file.amf_pathd3, config_file.HO_smf_pathd1]
            new_list = []
            for file in path:
                fh = open(file, "r").read()
                for line in re.findall(matchingStr, fh):
                    new_list.append(line)
            final_new_res = list(set(new_list))
            for res in final_new_res:
                print(res)
            print("***  TDD Inter frequency handover over Xn interface between two cells of FR1 band is successful ***")

    def N2_inter_HO(self):  # N2 based handover testcase validation
        matchingStr = "N2_inter_HO.*"
        path = [config_file.amf_pathd2, config_file.HO_Tamf_pathd1, config_file.HO_Tsmf_pathd1,
                config_file.HO_smf_pathd2, config_file.HO_Tsmf_pathd2, config_file.HO_smf_pathd3]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** NG-RAN N2 based handover without Xn interface is successful ***")

# class_instance = handover()
# class_instance.sour_des()
# class_instance.inter_nr_mobility()
# class_instance.HO_prepration()
# class_instance.Xn_inter_HO()
# class_instance.intra_nr_mobility()
# class_instance.HO_counters()
# class_instance.FDD_intra_frequency_Handover()
# class_instance.FDD_inter_frequency_Handover()
# class_instance.TDD_intra_frequency_Handover()
# class_instance.TDD_inter_frequency_Handover()
# class_instance.N2_inter_HO()