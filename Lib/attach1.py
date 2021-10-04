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
        #source for core
        source5 = config_file.path1
        source6 = config_file.path2
        source7 = config_file.new_amf_spath
        source8 = config_file.old_amf_spath
        source9 = config_file.ausf_spath
        source10 = config_file.udm_spath
        source11 = config_file.eir_spath
        source12 = config_file.pcf_spath
        source13 = config_file.smf_spath
        source14 = config_file.n3iwf_spath
        # Destination path
        destination1 = config_file.up1_path
        destination2 = config_file.du1_path
        destination3 = config_file.cp1_path
        # destination for core
        destination4 = config_file.gnb_npath
        destination5 = config_file.ue_npath
        destination6 = config_file.new_amf_npath
        destination7 = config_file.old_amf_npath
        destination8 = config_file.ausf_npath
        destination9 = config_file.udm_npath
        destination10 = config_file.eir_npath
        destination11 = config_file.pcf_npath
        destination12 = config_file.smf_npath
        destination13 = config_file.n3iwf_npath

        # source to destination
        dest = shutil.copy(source1, destination1)
        dest1 = shutil.move(source1, destination2)
        dest2 = shutil.move(source2, destination3)
        dest3 = shutil.move(source3, destination3)
        dest4 = shutil.move(source4, destination3)
        # source to destination core
        dest5 = shutil.copy(source5, destination4)
        dest6 = shutil.copy(source6, destination5)
        dest7 = shutil.copy(source7, destination7)
        dest8 = shutil.copy(source8, destination6)
        dest9 = shutil.copy(source7, destination5)
        dest10 = shutil.move(source5, destination6)
        dest11 = shutil.copy(source7, destination8)
        dest12 = shutil.copy(source9, destination9)
        dest13 = shutil.copy(source10, destination8)
        dest14 = shutil.move(source9, destination6)
        dest15 = shutil.copy(source7, destination4)
        dest16 = shutil.move(source6, destination6)
        dest17 = shutil.copy(source7, destination10)
        dest18 = shutil.move(source11, destination6)
        dest19 = shutil.copy(source7, destination9)
        dest20 = shutil.move(source10, destination6)
        dest21 = shutil.move(source8, destination9)
        dest22 = shutil.copy(source7, destination11)
        dest23 = shutil.move(source12, destination6)
        dest24 = shutil.copy(source7, destination12)
        dest25 = shutil.move(source13, destination6)
        dest26 = shutil.move(source7, destination13)
        dest27 = shutil.move(source14, destination6)



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
        print("*** UL and DL data path is working ***")

    def int_reg_val(self):
        #Rach request message validation
        string1 = config_file.message_22
        string2 = config_file.message_24
        string3 = config_file.message_25
        string4 = config_file.message_26
        string5 = config_file.message_27
        string6 = config_file.message_28
        string7 = config_file.message_29
        string8 = config_file.message_30
        string9 = config_file.message_31
        string10 = config_file.message_32
        string11 = config_file.message_33
        string12 = config_file.message_34
        string13 = config_file.message_35
        string14 = config_file.message_36
        string15 = config_file.message_37
        string16 = config_file.message_38
        string17 = config_file.message_39
        string18 = config_file.message_40
        string19 = config_file.message_41
        string20 = config_file.message_42
        string21 = config_file.message_43
        string22 = config_file.message_44
        string23 = config_file.message_45
        string24 = config_file.message_46
        string25 = config_file.message_47
        string26 = config_file.message_48
        string27 = config_file.message_49
        string28 = config_file.message_50
        string29 = config_file.message_51

        # opening a text file
        file1 = open(config_file.udm_pathd1, "r")
        file2 = open(config_file.udm_pathd2, "r")
        file3 = open(config_file.udm_pathd3, "r")
        file4 = open(config_file.smf_pathd1, "r")
        file5 = open(config_file.pcf_pathd1, "r")
        file6 = open(config_file.old_amf_pathd1, "r")
        file7 = open(config_file.new_amf_pathd1, "r")
        file8 = open(config_file.new_amf_pathd2, "r")
        file9 = open(config_file.new_amf_pathd3, "r")
        file10 = open(config_file.new_amf_pathd4, "r")
        file11 = open(config_file.new_amf_pathd5, "r")
        file12 = open(config_file.new_amf_pathd6, "r")
        file13 = open(config_file.new_amf_pathd7, "r")
        file14 = open(config_file.new_amf_pathd8, "r")
        file15 = open(config_file.new_amf_pathd9, "r")
        file16 = open(config_file.n3iwf_pathd1, "r")
        file17 = open(config_file.eir_pathd1, "r")
        file18 = open(config_file.ausf_pathd1, "r")
        file19 = open(config_file.ausf_pathd2, "r")
        file20 = open(config_file.path3, "r")
        file21 = open(config_file.path4, "r")
        file22 = open(config_file.ue_pathd1, "r")
        file23 = open(config_file.gnb_pathd1, "r")


        # read file content
        readfile1 = file1.read()
        readfile2 = file2.read()
        readfile3 = file3.read()
        readfile4 = file4.read()
        readfile5 = file5.read()
        readfile6 = file6.read()
        readfile7 = file7.read()
        readfile8 = file8.read()
        readfile9 = file9.read()
        readfile10 = file10.read()
        readfile11 = file11.read()
        readfile12 = file12.read()
        readfile13 = file13.read()
        readfile14 = file14.read()
        readfile15 = file15.read()
        readfile16 = file16.read()
        readfile17 = file17.read()
        readfile18 = file18.read()
        readfile19 = file19.read()
        readfile20 = file20.read()
        readfile21 = file21.read()
        readfile22 = file22.read()
        readfile23 = file23.read()

        # checking condition for string found or not
        if string1 in readfile20 and string1 in readfile9:
            print(string1, 'Found In File')
        if string2 in readfile6 and string3 in readfile11:
            print(string2, string3, 'Found In File')
        if string4 in readfile22 and string5 in readfile15:
            print(string4, string5, 'Found In File')
        if string6 in readfile18 and string7 in readfile1:
            print(string6, string7, 'Found In File')
        if string8 in readfile19 and string9 in readfile7:
            print(string8, string9, 'Found In File')
        if string10 in readfile23 and string11 in readfile9:
            print(string10, string11, 'Found In File')
        if string12 in readfile23 and string13 in readfile9:
            print(string12, string13, 'Found In File')
        if string14 in readfile17 and string15 in readfile8:
            print(string14, string15, 'Found In File')
        if string16 in readfile2 and string17 in readfile14:
            print(string16, string17, 'Found In File')
        if string18 in readfile2 and string19 in readfile14:
            print(string18, string19, 'Found In File')
        if string20 in readfile3 and string21 in readfile5:
            print(string20, string21, 'Found In File')
        if string22 in readfile12 and string23 in readfile4:
            print(string22, string23, 'Found In File')
        if string24 in readfile13 and string25 in readfile16:
            print(string24, string25, 'Found In File')
        if string26 in readfile10 and string27 in readfile22:
            print(string26, string27, 'Found In File')
        if string28 in readfile15:
            print(string28, 'Found In File')
        if string29 in readfile2 and string29 in readfile14:
            print(string29, 'Found In File')
        else:
            raise Exception("messages not found")

            # closing a file
        file1.close()
        print("*** Initial registration is successfull ***")

    def crct_hni_val(self):
        string4 = config_file.message_26
        string5 = config_file.message_27
        string6 = config_file.message_28
        string7 = config_file.message_29
        string8 = config_file.message_30
        string9 = config_file.message_31
        string10 = config_file.message_32
        string11 = config_file.message_33
        string12 = config_file.message_34
        string13 = config_file.message_35
        string27 = config_file.message_49

        file15 = open(config_file.new_amf_pathd9, "r")
        file22 = open(config_file.ue_pathd1, "r")
        file7 = open(config_file.new_amf_pathd1, "r")
        file18 = open(config_file.ausf_pathd1, "r")
        file1 = open(config_file.udm_pathd1, "r")
        file19 = open(config_file.ausf_pathd2, "r")
        file23 = open(config_file.gnb_pathd1, "r")
        file9 = open(config_file.new_amf_pathd3, "r")

        readfile1 = file1.read()
        readfile15 = file15.read()
        readfile22 = file22.read()
        readfile7 = file7.read()
        readfile18 = file18.read()
        readfile19 = file19.read()
        readfile23 = file23.read()
        readfile9 = file9.read()

        if string4 in readfile22 and string5 in readfile15:
            print(string4, string5, 'Found In File')
        if string6 in readfile18 and string7 in readfile1:
            print(string6, string7, 'Found In File')
        if string8 in readfile19 and string9 in readfile7:
            print(string8, string9, 'Found In File')
        if string10 in readfile23 and string12 in readfile23:
            print(string10, string12, 'Found In File')
        if string11 in readfile9 and string13 in readfile9:
            print(string8, string9, 'Found In File')
        if string27 in readfile22:
            print(string27, 'Found In File')

        else:
            raise Exception("messages not found")

        # closing a file
        file1.close()
        print("*** Successfully performed initial registration with correct HNI ***")

# class_instance = attach1()
# class_instance.copy_file()
# class_instance.int_reg_val()
# class_instance.b_setup_val()
# class_instance.b_release_val()
