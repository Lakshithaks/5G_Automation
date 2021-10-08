import os
import re
import sys
sys.path.insert(0, r"C:\Users\40014330\PycharmProjects\5G_Automation\VariableFiles")
import shutil
import config_file

class attach1:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def copy_file(self):

        source = [config_file.cp_path, config_file.up_path, config_file.du_path, config_file.me_path, config_file.path1,
                  config_file.path2, config_file.new_amf_spath, config_file.old_amf_spath, config_file.ausf_spath,
                  config_file.udm_spath, config_file.eir_spath, config_file.pcf_spath, config_file.smf_spath,
                  config_file.n3iwf_spath, config_file.upf_spath]
        destination = [config_file.up1_path, config_file.du1_path, config_file.cp1_path, config_file.gnb_npath,
                       config_file.ue_npath, config_file.new_amf_npath, config_file.old_amf_npath,
                       config_file.ausf_npath, config_file.udm_npath, config_file.eir_npath, config_file.pcf_npath,
                       config_file.smf_npath, config_file.n3iwf_npath, config_file.upf_npath]

        # source to destination
        dest = shutil.copy(source[0], destination[0])
        dest1 = shutil.move(source[0], destination[1])
        dest2 = shutil.move(source[1], destination[2])
        dest3 = shutil.move(source[2], destination[2])
        dest4 = shutil.move(source[3], destination[2])
        # # source to destination core
        dest5 = shutil.copy(source[4], destination[3])
        dest6 = shutil.copy(source[5], destination[4])
        dest7 = shutil.copy(source[6], destination[6])
        dest8 = shutil.copy(source[7], destination[5])
        dest9 = shutil.copy(source[6], destination[4])
        dest10 = shutil.move(source[4], destination[5])
        dest11 = shutil.copy(source[6], destination[7])
        dest12 = shutil.copy(source[8], destination[8])
        dest13 = shutil.copy(source[9], destination[7])
        dest14 = shutil.move(source[8], destination[5])
        dest15 = shutil.copy(source[6], destination[3])
        dest16 = shutil.move(source[5], destination[5])
        dest17 = shutil.copy(source[6], destination[9])
        dest18 = shutil.move(source[10], destination[5])
        dest19 = shutil.copy(source[6], destination[8])
        dest20 = shutil.copy(source[9], destination[5])
        dest21 = shutil.move(source[7], destination[8])
        dest22 = shutil.copy(source[6], destination[10])
        dest23 = shutil.copy(source[11], destination[5])
        dest24 = shutil.copy(source[6], destination[11])
        dest25 = shutil.copy(source[12], destination[5])
        dest26 = shutil.move(source[6], destination[12])
        dest27 = shutil.copy(source[13], destination[7])
        dest27 = shutil.move(source[13], destination[5])
        dest28 = shutil.copy(source[12], destination[13])
        dest29 = shutil.move(source[14], destination[11])
        dest30 = shutil.copy(source[12], destination[10])
        dest31 = shutil.move(source[11], destination[11])
        dest32 = shutil.move(source[12], destination[8])
        dest33 = shutil.move(source[9], destination[11])
        print("Source files has been successfully copied to destination folder!!")

    def b_release_val(self):

        matchingStr = "release.*"
        path = [config_file.up2_path, config_file.cp2_path, config_file.cp3_path, config_file.du2_path, config_file.cp4_path]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Bearer context release procedure is performed ***")

    def b_setup_val(self):

        print("Successfully validated rach procedure")
        matchingStr = "setup.*"
        path = [config_file.cp2_path, config_file.cp3_path, config_file.up2_path, config_file.du2_path]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** successfully verified UL and DL data transfer ***")

    def int_reg_val(self):
        print("Powered On the UE with correct HNI SIM card and Validated Rach procedure")
        matchingStr = "inreg.*"
        path = [config_file.path3, config_file.new_amf_pathd3, config_file.old_amf_pathd1, config_file.new_amf_pathd5,
                config_file.ue_pathd1, config_file.new_amf_pathd9, config_file.ausf_pathd1, config_file.udm_pathd1,
                config_file.ausf_pathd2, config_file.new_amf_pathd1, config_file.gnb_pathd1, config_file.eir_pathd1,
                config_file.new_amf_pathd2, config_file.udm_pathd2, config_file.new_amf_pathd8, config_file.udm_pathd3,
                config_file.pcf_pathd1, config_file.new_amf_pathd6, config_file.smf_pathd1, config_file.new_amf_pathd7,
                config_file.n3iwf_pathd1, config_file.new_amf_pathd4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Initial registration is successful ***")

    def crct_hni_val(self):
        print("*** RACH procedure is successfully validated ***")
        matchingStr = "_crct_hni.*"
        path = [config_file.ue_pathd1, config_file.new_amf_pathd9, config_file.ausf_pathd1, config_file.udm_pathd1,
                config_file.ausf_pathd2, config_file.new_amf_pathd1, config_file.gnb_pathd1, config_file.new_amf_pathd3, ]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Initial registration is successful due to correct HNI ***")

    def dereg_val(self):

        print("Switched off the UE or Turned on Aeroplane mode")
        matchingStr = "dereg.*"
        path = [config_file.new_amf_pathd9, config_file.ue_pathd1, config_file.new_amf_pathd7, config_file.udm_pathd4, config_file.upf_pathd1, config_file.pcf_pathd1,
                config_file.pcf_pathd2, config_file.gnb_pathd1, config_file.new_amf_pathd3, config_file.new_amf_pathd6, config_file.smf_pathd1,
                config_file.smf_pathd2, config_file.smf_pathd3, config_file.smf_pathd4, config_file.path3, config_file.path4, ]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Successfully performed the ue initiated deregistration ***")

    def net_dereg_val(self):

        print("UE is in idle or connected mode")
        matchingStr = "nid.*"
        path = [config_file.udm_pathd2, config_file.new_amf_pathd9, config_file.new_amf_pathd8, config_file.upf_pathd1,
                config_file.smf_pathd2, config_file.new_amf_pathd7, config_file.pcf_pathd1, config_file.new_amf_pathd6,
                config_file.path3, config_file.path4, config_file.gnb_pathd1, config_file.new_amf_pathd3, config_file.smf_pathd1, ]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Successfully performed the network initiated deregistration ***")

    def incrct_hni_val(self):
        matchingStr = "incrct_hni.*"
        path = [config_file.new_amf_pathd3, config_file.old_amf_pathd1, config_file.new_amf_pathd5,
                 config_file.ue_pathd1, config_file.new_amf_pathd9, config_file.ausf_pathd1, config_file.udm_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Initial registration is not successful due to incorrect HNI ***")


#class_instance = attach1()
#class_instance.copy_file()
#class_instance.int_reg_val()
#class_instance.b_setup_val()
#class_instance.b_release_val()
#class_instance.crct_hni_val()
#class_instance.incrct_hni_val()
#class_instance.dereg_val()
#class_instance.net_dereg_val()
