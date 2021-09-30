import os
import sys
sys.path.insert(0, r"C:\Users\Admin\PycharmProjects\5G_Automation\VariableFiles")
import shutil
import config_file

class attach1:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def copy_file(self):
        """copy request message"""
        # path
        #path = 'C:\AUTOMATION\Locker'

        # Source path
        source1 = config_file.cp_path
        source2 = config_file.up_path
        source3 = config_file.du_path
        source4 = config_file.me_path
        # Destination path
        destination1 = config_file.up1_path
        destination2 = config_file.du1_path
        destination3 = config_file.cp1_path

         # source to destination
        dest = shutil.copy(source1, destination1)
        dest1 = shutil.move(source1, destination2)
        dest2 = shutil.move(source2, destination3)
        dest3 = shutil.move(source3, destination3)
        dest4 = shutil.move(source4, destination3)

        print("Source files has been successfully copied to destination folder!!")

    def b_release_val(self):
        #Rach request message validation
        string1 = config_file.message_9
        string2 = config_file.message_10
        string3 = config_file.message_11
        string4 = config_file.message_12
        string5 = config_file.message_13
        string6 = config_file.message_14
        string7 = config_file.message_15

        # opening a text file
        file1 = open(config_file.cp2_path, "r")
        file2 = open(config_file.cp3_path, "r")
        file3 = open(config_file.cp4_path, "r")
        file4 = open(config_file.up2_path, "r")
        file5 = open(config_file.du2_path, "r")

        # read file content
        readfile1 = file1.read()
        readfile2 = file2.read()
        readfile3 = file3.read()
        readfile4 = file4.read()
        readfile5 = file5.read()

        # checking condition for string found or not
        if string2 in readfile1 and string7 in readfile1:
            print(string2, string7, 'Found In File')
        if string3 in readfile2 and string6 in readfile2:
            print(string3, string6, 'Found In File')
        if string4 in readfile3:
            print(string4,'Found In File')
        if string1 in readfile4 and string5 in readfile4:
            print(string1, string5, 'Found In File')
        if string3 in readfile5 and string6 in readfile5:
            print(string3, string6, 'Found In File')

        else:
            raise Exception("messages not found")

            # closing a file
        file1.close()
        print("*** Bearer context release procedure is performed ***")


    def b_setup_val(self):
        # Rach request message validation
        string1 = config_file.message_9
        string2 = config_file.message_10
        string8 = config_file.message_16
        string9 = config_file.message_18
        string10 = config_file.message_17

        # opening a text file
        file1 = open(config_file.cp2_path, "r")
        file2 = open(config_file.cp3_path, "r")
        file4 = open(config_file.up2_path, "r")
        file5 = open(config_file.du2_path, "r")

        # read file content
        readfile1 = file1.read()
        readfile2 = file2.read()
        readfile4 = file4.read()
        readfile5 = file5.read()

        # checking condition for string found or not
        if string8 in readfile4 and string9 in readfile4:
                print(string8, string9, 'Found In File')
        if string10 in readfile1 and string2 in readfile1:
                print(string10,string2, 'Found In File')
        if string9 in readfile2 and string9 in readfile5:
                print(string9, 'Found In File')
        if string1 in readfile4:
                print(string1, 'Found In File')


        else:
            raise Exception("messages not found")

        # closing a file
        file1.close()
        print("*** Bearer context setup procedure is performed ***")


# class_instance = attach1()
# class_instance.copy_file()
# class_instance.b_setup_val()
# class_instance.b_release_val()
