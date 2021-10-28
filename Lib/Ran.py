"""
Case name: RAN
Author: Priyanka and Lakshitha
How to execute testcase: robot -t "test case name" -d Report Testsuite/5G_Testsuite.robot
"""
import re
import sys
sys.path.insert(0, r"C:\Users\Admin\PycharmProjects\5G_Automation\VariableFiles")
# sys.path.append("/VariableFiles")
import config_file
import shutil

class Ran:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'  # setting library scope as global

    def __init__(self):
        pass
    def UE_context_release_request_DU_intiated(self):  # Passing messages of this testcase to file
       IE_1 = {"Message_Type": 1, "gNB_CU_UE_F1AP_ID": 5, "gNB_DU_UE_F1AP_ID": 4, "Cause": "Unknown" }
       with open(config_file.du_spath,"a") as data:
           data.write("\nUE_con_rel_req_du_inti-UE CONTEXT RELEASE REQUEST "+str(IE_1))

    def mov_ran_files(self):    # Moving files from source to destination
        source = [config_file.du_spath, config_file.cu_spath, config_file.cn_spath, config_file.ran_gnb_spath]
        destination = [config_file.cn_npath, config_file.cu_npath, config_file.du_npath, config_file.ran_gnb_npath]

        # source to destination
        dest1 = shutil.move(source[0], destination[1])
        dest2 = shutil.copy(source[1], destination[0])
        dest1 = shutil.move(source[2], destination[1])
        dest2 = shutil.copy(source[1], destination[2])
        dest1 = shutil.move(source[1], destination[3])
        dest2 = shutil.move(source[3], destination[1])

    def F1_NG_Setup(self):  # F1 setup testcase validation
        print("The gNB-DU and its cells are configured by OAM in the F1 pre-operational state")
        matchingStr = "F1_NG_setup.*"
        path = [config_file.ran_gnb_pathd1, config_file.cn_pathd1, config_file.cu_pathd1, config_file.cu_pathd2,
                config_file.cu_pathd3, config_file.du_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** F1 interface btw gNB-DU and a gNB-CU, cell activation and UL &DL data transfer is successful ***")

    def F1_Set_Fail(self):  # F1 setup failure testcase validation
        matchingStr = "F1_set_fail.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("***  Verified the  F1 Setup procedure failure/Unsuccessful Operation ***")

    def F1_Set_DU_Removal_Suc(self):   # F1 setup removal(DU) testcase validation
        matchingStr = "F1_set_rem_du_suc.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified F1 Setup Removal Procedure gNB DU Request Successfully ***")

    def F1_Set_DU_Removal_Fail(self):   # F1setup removal(DU) failure testcase validation
        matchingStr = "F1_set_rem_du_fail.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified F1 Setup Removal Procedure gNB DU Request Failure Operations ***")

    def F1_Set_CU_Removal_Suc(self):  # F1 setup removal(CU) testcase validation
        matchingStr = "F1_set_rem_cu_suc.*"
        path = [config_file.cu_pathd1, config_file.du_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified F1 Setup Removal Procedure gNB CU Request Successfully ***")

    def F1_Set_CU_Removal_Fail(self):  # F1 setup removal(CU) failure testcase validation
        matchingStr = "F1_set_rem_cu_fail.*"
        path = [config_file.cu_pathd1, config_file.du_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified F1 Setup Removal Procedure gNB CU Request Failure Operations ***")

    def DU_Con_Update_Suc(self):   # Configuration update(DU) testcase validation
        matchingStr = "du_con_up_suc.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified GNB-DU configuration update procedure successful ***")

    def DU_Con_Update_Fail(self):   # Configuration update(DU) failure testcase validation
        matchingStr = "du_con_up_fail.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified GNB-DU configuration update procedure Failure Operations ***")

    def CU_Con_Update_Suc(self):    # Configuration update(CU) testcase validation
        matchingStr = "cu_con_up_suc.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified GNB-CU configuration update procedure Successful ***")

    def CU_Con_Update_Fail(self):   # Configuration update(CU) failure testcase validation
        matchingStr = "cu_con_up_fail.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified GNB-CU configuration update procedure Failure Operations ***")

    def UE_con_setup_success(self):   # UE Context setup testcase validation
        matchingStr = "UE_con_set_suc.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified the UE CONTEXT SETUP ***")

    def UE_con_setup_failure(self):   # UE Context setup failure testcase validation
        matchingStr = "UE_con_set_fail.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified the UE CONTEXT SETUP failure ***")

    def UE_con_rel_DU(self):   # UE Context release(DU) testcase validation
        matchingStr = "UE_con_rel_req_du_inti.*"
        path = [config_file.du_pathd1, config_file.cu_pathd1]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified the UE CONTEXT SETUP failure ***")


# class_instance = Ran()
# class_instance.mov_ran_files()
# class_instance.N2_NG_Setup()
# class_instance.UE_context_release_request_DU_intiated()