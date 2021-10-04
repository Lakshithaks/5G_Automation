import os
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

    def unlock(self):

        # Unlock the folder
        pw = config_file.pw

        # while True:
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
                    # break

            else:
                print("Locker folder is not LOCKED")

        else:
            print("wrong password! Try again later")
            # break

    def copy_gnb_ue(self):

        # Source path
        source5 = config_file.path1
        source6 = config_file.path2

        # Destination path
        destination4 = 'D:\TestCases\Locker\gNB'
        destination5 = 'D:\TestCases\Locker\-UE'

        # source to destination
        dest5 = shutil.move(source5, destination4)
        dest6 = shutil.move(source6, destination5)
        print("Successfully moved the file")

    def rach_req_val(self):
        string1 = config_file.message_1
        string3 = config_file.message_3

        # opening a text file
        file1 = open(config_file.path3, "r")

        # read file content
        readfile = file1.read()

        # checking condition for string found or not
        if string1 in readfile and string3 in readfile:
            print(string1, string3, 'Found In Request File')

        else:
            raise Exception("Messages not found")
            #print('Not Found')

            # closing a file
        file1.close()

    def eps_req_val(self):

        string5 = config_file.message_5

        # opening a text file
        file1 = open(config_file.path3, "r")

        # read file content
        readfile = file1.read()

        # checking condition for string found or not

        if string5 in readfile:
            print(string5, 'Found In Response File')

        else:
            raise Exception("Messages not found")
            #print('Not Found')

            # closing a file
        file1.close()
    def apn_req_val(self):

        string7 = config_file.message_7

        # opening a text file
        file1 = open(config_file.path3, "r")

        # read file content
        readfile = file1.read()

        # checking condition for string found or not

        if string7 in readfile:
            print(string7, 'Found In Response File')

        else:
            raise Exception("Messages not found")
            #print('Not Found')

            # closing a file
        file1.close()

    def rach_res_val(self):
        string2 = config_file.message_2
        string4 = config_file.message_4

        # opening a text file
        file2 = open(config_file.path4, "r")

        # read file content
        readfile = file2.read()

        # checking condition for string found or not
        if string2 in readfile and string4 in readfile:
            print(string2, string4, 'Found In Response File')

        else:
            raise Exception("Messages not found")
            #print('Not Found')

            # closing a file
        file2.close()

    def eps_res_val(self):

        string6 = config_file.message_6

        # opening a text file
        file2 = open(config_file.path4, "r")

        # read file content
        readfile = file2.read()

        # checking condition for string found or not
        if string6 in readfile:
            print(string6, 'Found In Response File')

        else:
            raise Exception("Messages not found")
            #print('Not Found')

            # closing a file
        file2.close()

    def apn_res_val(self):
        string8 = config_file.message_8

        # opening a text file
        file2 = open(config_file.path4, "r")

        # read file content
        readfile = file2.read()

        # checking condition for string found or not
        if string8 in readfile:
            print(string8, 'Found In Response File')

        else:
            raise Exception("Messages not found")
            #print('Not Found')

            # closing a file
        file2.close()


    def srb_val(self):

        string1 = config_file.message_19
        string2 = config_file.message_21
        string3 = config_file.message_20

        # opening a text file
        file1 = open(config_file.path3, "r")
        file2 = open(config_file.path4, "r")

        # read file content
        readfile1 = file1.read()
        readfile2 = file2.read()

        # checking condition for string found or not

        if string1 in readfile1 and string2 in readfile1:
            print(string1, string2, 'Found In File')
        if string3 in readfile2:
            print(string3, 'Found In File')

        else:
            raise Exception("Messages not found")
        print("SRB1 setup procedure is performed")
        file1.close()
        file2.close()    # closing a file

    def barred_val(self):

        string1 = config_file.message_22
        string2 = config_file.message_23

        # opening a text file
        file1 = open(config_file.path3, "r")
        file2 = open(config_file.path4, "r")

        # read file content
        readfile1 = file1.read()
        readfile2 = file2.read()

        # checking condition for string found or not
        if string1 in readfile1 and string2 in readfile2:
            print(string1, string2, 'Found In File')

        else:
            raise Exception("Messages not found")
            # print('Not Found')

            # closing a file
        file1.close()
        file2.close()

    def delete(self):

        f1 = open(config_file.path3, 'r')
        f2 = open(config_file.path4, 'r')

        a = [config_file.message_1, config_file.message_3, config_file.message_5, config_file.message_7]
        b = [config_file.message_2, config_file.message_4, config_file.message_6, config_file.message_8]
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

    def lock(self):  # lock the folder

        p_w = config_file.pw

        # while True:
        pw1 = config_file.pw1
        if p_w == pw1:
            os.chdir(config_file.dir_path)
            # print("Your path Successfully Changed")
            # If Locker folder or Recycle bin does not exist then we will be create Locker Folder

            if os.path.exists(config_file.loc_path):
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # sys.exit()
                # break

            else:
                os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # break

        else:
            print("wrong password! Try again later")
            # break



#class_instance = attach_function()
# class_instance.unlock()
#class_instance.copy_gnb_ue()
# class_instance.rach_req_val()
# class_instance.rach_res_val()
#class_instance.srb_val()
# class_instance.delete()
# class_instance.lock()

