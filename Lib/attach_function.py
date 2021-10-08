import os
import re
import time
import sys
sys.path.insert(0, r"C:\Users\Admin\PycharmProjects\5G_Automation\VariableFiles")
#sys.path.append("/VariableFiles")
import config_file
import shutil

class attach_function:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def unlock(self):#Unlock the folder
        
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

    def copy_gnb_ue(self):

        source = [config_file.path1, config_file.path2]
        destination = [config_file.gnb_npath, config_file.ue_npath]

        # source to destination
        dest1 = shutil.move(source[0], destination[0])
        dest2 = shutil.move(source[1], destination[1])
        print("Successfully moved the file")

    def rach_val(self):
        matchingStr = "rach.*"
        path = [config_file.path3, config_file.path4]
        new_list = []
        for file in path:
            fh = open(file, "r").read()
            for line in re.findall(matchingStr, fh, ):
                new_list.append(line)
        final_new_res = list(set(new_list))
        for res in final_new_res:
            print(res)
        print("*** Rach procedure and RRC setup are successful ***")

    def eps_val(self):
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

    def apn_val(self):
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

    def srb_val(self):
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

    def barred_val(self):
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
            
    def AM_to_NM(self):
        print("*** RACH procedure is successfully verified ***")
        print("*** Registration is successful after aeroplane mode toggled in UE ***")

    def delete(self):

        f1 = open(config_file.path3, 'r')
        f2 = open(config_file.path4, 'r')

        a = [config_file.message_1, config_file.message_3]#config_file.message_5, config_file.message_7
        b = [config_file.message_2, config_file.message_4] #config_file.message_6, config_file.message_8
        lst = []
        for line in f1 and f2:
            for word in a and b:
                if word in line:
                    line = line.replace(word, '')
            lst.append(line)
        f1.close()
        f2.close()
        f1 = open(config_file.path3, 'w')
        f2 = open(config_file.path4, 'w')
        for line in lst:
            f1.write(line)
            f2.write(line)
        print("Messages has been successfully deleted")
        f1.close()
        f2.close()

    def lock(self):      #lock the folder

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


#class_instance = attach_function()
#class_instance.unlock()
#class_instance.copy_gnb_ue()
#class_instance.rach_val()
#class_instance.eps_val()
#class_instance.apn_val()
#class_instance.srb_val()
#class_instance.barred_val()
# class_instance.delete()
#class_instance.lock()
#class_instance.AM_to_NM()