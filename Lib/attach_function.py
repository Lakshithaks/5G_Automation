import os
import time
import sys
sys.path.insert(0, r"C:\Users\Admin\PycharmProjects\5G_Automation\Variablefile")
import config_file
import shutil


class attach_function:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def unlock(self):
        pw = config_file.pw

        while True:
            pw1 = config_file.pw1
            if pw1 == pw:
                os.chdir("C:\AUTOMATION")


                if not os.path.exists(r"C:\AUTOMATION\Locker"):

                    if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):

                        os.mkdir("Locker")

                        print("Locker Folder Successfully created")

                    else:

                        os.popen('attrib -h -s -r Locker')

                        os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")

                        print("Locker Folder has been Successfully Unlocked")

                        break

                else:
                    print("wrong password! Try again later")
            break
    def copy_req(self):

        # path
        path = 'C:\AUTOMATION\Locker'

        # Source path
        source = config_file.path1

        # Destination path
        destination = 'C:\AUTOMATION\Locker\GNB'

        # source to destination
        dest = shutil.move(source, destination)
        print("Successfully copied Request.txt to gNB folder")


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
            raise Exception("messages not found")

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
            raise Exception("messages not found")

            # closing a file
        file1.close()

    def copy_res(self):

        # path
        path = 'C:\AUTOMATION\Locker'

        # Source path
        source1 = config_file.path2

        # Destination path
        destination1 = 'C:\AUTOMATION\Locker\-UE'

        # source to destination
        dest1 = shutil.move(source1, destination1)
        print("Successfully copied Response.txt to UE folder")

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
            raise Exception("messages not found")

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
            raise Exception("messages not found")

            # closing a file
        file2.close()

    def delete(self):

        f1 = open(config_file.path3, 'r')
        f2 = open(config_file.path4, 'r')

        a = [config_file.message_1, config_file.message_3, config_file.message_5]
        b = [config_file.message_2, config_file.message_4, config_file.message_6]
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

    def lock(self):
        pw = "password"

        while True:
            pw1 = "password"
            if pw == pw1:
                os.chdir("C:\AUTOMATION")
                # print("Your path Successfully Changed")
                # If Locker folder or Recycle bin does not exist then we will be create Locker Folder

                if os.path.exists(r"C:\AUTOMATION\Locker"):
                    os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")

                    os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')

                    print("Locker folder has been successfully locked")

                    sys.exit()

                else:
                    os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")

                    os.mkdir("Locker")

                    print("Locker Folder Successfully created")


            else:
                print("wrong password! Try again later")
                break


# class_instance=attach_function()
# class_instance.unlock()
# class_instance.copy_req()
# class_instance.req_val()
# class_instance.copy_res()
# class_instance.res_val()
# class_instance.delete()
# class_instance.lock()