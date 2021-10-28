"""
Case name: Attach
Author: Lakshitha and Priyanka
How to execute testcase: robot -t "test case name" -d Report Testsuite/5G_Testsuite.robot
"""
import os
import re
import sys
sys.path.insert(0, r"C:\Users\40014330\PycharmProjects\5G_Automation\VariableFiles")
#sys.path.append("/VariableFiles")
import config_file
import shutil

class attach_function:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'  # setting library scope as global

    def __init__(self):
        pass

    def unlock(self):  # Function to Unlock the folder

        pw = config_file.pw
        pw1 = config_file.pw1
        if pw1 == pw:
            os.chdir(config_file.dir_path)
            if not os.path.exists(config_file.loc_path):
                if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                    os.mkdir("Locker")
                    print("Locker Folder Successfully created")

                else:
                    os.popen('attrib -h -s -r Locker')
                    os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                    print("Locker Folder has been Successfully Unlocked")

            else:
                print("Locker folder is not LOCKED")

        else:
            print("wrong password! Try again later")

    def copy_gnb_ue(self):  # Moving files from source to destination

        source = [config_file.path1, config_file.path2]
        destination = [config_file.gnb_npath, config_file.ue_npath]

        # source to destination
        dest1 = shutil.move(source[0], destination[0])
        dest2 = shutil.move(source[1], destination[1])
        print("Successfully moved the file")

    def rach_val(self):  # RACH testcase validation
        matchingStr = "rach.*"  # validation string
        path = [config_file.path3, config_file.path4]  # validation paths
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Rach procedure and RRC setup are successful ***")

    def eps_val(self):  # EPS/IMSI registration testcase validation
        matchingStr = "eps.*"
        path = [config_file.path3, config_file.path4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("Combined EPS/IMSI Registration is successful")

    def apn_val(self):  # incorrect APN name validation
        matchingStr = "apn.*"
        path = [config_file.path3, config_file.path4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print(" Registration Reject with incorrect configured APN")

    def srb_val(self):  # srb setup procedure testcase validation
        print("Successfully validated rach procedure")
        matchingStr = "srb.*"
        path = [config_file.path3, config_file.path4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("SRB1 is established successfully ")

    def barred_val(self):  # cell barred testcase validation
        matchingStr = "barred.*"
        path = [config_file.path3, config_file.path4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)

    def AM_to_NM(self):  # Aeroplane mode to normal mode validation
        print("*** RACH procedure is successfully verified ***")
        print("*** Registration is successful after aeroplane mode toggled in UE ***")

    def mib_sib(self):  # MIB & SIB decoding validation
        matchingStr = "mib_sib.*"
        path = [config_file.path3, config_file.path4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Verified Rach, Initial Registration and MIB and SIB are decoded successfully ***")

    def lock(self):  # lock the folder

        p_w = config_file.pw
        pw1 = config_file.pw1
        if p_w == pw1:
            os.chdir(config_file.dir_path)

            if os.path.exists(config_file.loc_path):

                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")

            else:
                os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")

        else:
            print("wrong password! Try again later")

# class_instance = attach_function()
# class_instance.unlock()
# class_instance.copy_gnb_ue()
# class_instance.rach_val()
# class_instance.eps_val()
# class_instance.apn_val()
# class_instance.srb_val()
# class_instance.barred_val()
# class_instance.delete()
# class_instance.lock()
# class_instance.AM_to_NM()