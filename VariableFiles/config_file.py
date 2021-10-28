"""
Case configuration part of main script
"""
# path for locker

dir_path = "D:\Testcase"
loc_path = "D:\Testcase\Locker"

#paths for gnb & ue
path1 = "D:\Testcase\Locker\Attach\-UE\msg_from_UE.txt"
path2 = "D:\Testcase\Locker\Attach\gNB\msg_from_gNB.txt"
path3 = "D:\Testcase\Locker\Attach\gNB\msg_from_UE.txt"
path4 = "D:\Testcase\Locker\Attach\-UE\msg_from_gNB.txt"
gnb_npath = "D:\Testcase\Locker\Attach\gNB"
ue_npath = "D:\Testcase\Locker\Attach\-UE"
ue_pathd1 = "D:\Testcase\Locker\Attach\-UE\msg_from_newAMF.txt"
gnb_pathd1 = "D:\Testcase\Locker\Attach\gNB\msg_from_newAMF.txt"

#password for locker
pw = "password"
pw1 = "password"

#path for cu,du & menb
cp_path = "D:\Testcase\Locker\Attach\gNB\CU-CP\msg_from_CUCP.txt"
cp1_path = "D:\Testcase\Locker\Attach\gNB\CU-CP"
cp2_path = "D:\Testcase\Locker\Attach\gNB\CU-CP\msg_from_CUUP.txt"
cp3_path = "D:\Testcase\Locker\Attach\gNB\CU-CP\msg_from_DU.txt"
cp4_path = "D:\Testcase\Locker\Attach\gNB\CU-CP\msg_from_Menb.txt"
up_path = "D:\Testcase\Locker\Attach\gNB\CU-UP\msg_from_CUUP.txt"
up1_path = "D:\Testcase\Locker\Attach\gNB\CU-UP"
up2_path = "D:\Testcase\Locker\Attach\gNB\CU-UP\msg_from_CUCP.txt"
du_path = "D:\Testcase\Locker\Attach\gNB\DU\msg_from_DU.txt"
du1_path = "D:\Testcase\Locker\Attach\gNB\DU"
du2_path = "D:\Testcase\Locker\Attach\gNB\DU\msg_from_CUCP.txt"
me_path = "D:\Testcase\Locker\Attach\MeNB\msg_from_Menb.txt"
me1_path = "D:\Testcase\Locker\Attach\MeNB"

#path for core compoents
ausf_npath = "D:\Testcase\Locker\Attach\CN\AUSF"
ausf_spath = "D:\Testcase\Locker\Attach\CN\AUSF\msg_from_AUSF.txt"
eir_npath = "D:\Testcase\Locker\Attach\CN\EIR"
eir_spath = "D:\Testcase\Locker\Attach\CN\EIR\msg_from_EIR.txt"
n3iwf_npath = "D:\Testcase\Locker\Attach\CN\-N3IWF"
n3iwf_spath = "D:\Testcase\Locker\Attach\CN\-N3IWF\msg_from_N3IWF.txt"
new_amf_npath = "D:\Testcase\Locker\Attach\CN\-New_AMF"
new_amf_spath = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_newAMF.txt"
old_amf_npath = "D:\Testcase\Locker\Attach\CN\Old_AMF"
old_amf_spath = "D:\Testcase\Locker\Attach\CN\Old_AMF\msg_from_oldAMF.txt"
pcf_npath = "D:\Testcase\Locker\Attach\CN\PCF"
pcf_spath = "D:\Testcase\Locker\Attach\CN\PCF\msg_from_PCF.txt"
smf_npath = "D:\Testcase\Locker\Attach\CN\SMF"
smf_spath = "D:\Testcase\Locker\Attach\CN\SMF\msg_from_SMF.txt"
udm_npath = "D:\Testcase\Locker\Attach\CN\-UDM"
udm_spath = "D:\Testcase\Locker\Attach\CN\-UDM\msg_from_UDM.txt"
upf_npath = "D:\Testcase\Locker\Attach\CN\-UPF"
upf_spath = "D:\Testcase\Locker\Attach\CN\-UPF\msg_from_UPF.txt"
smsf_npath = "D:\Testcase\Locker\Attach\CN\SMSF"
smsf_spath = "D:\Testcase\Locker\Attach\CN\SMSF\msg_from_SMSF.txt"

#core validation paths
udm_pathd1 = "D:\Testcase\Locker\Attach\CN\-UDM\msg_from_AUSF.txt"
udm_pathd2 = "D:\Testcase\Locker\Attach\CN\-UDM\msg_from_newAMF.txt"
udm_pathd3 = "D:\Testcase\Locker\Attach\CN\-UDM\msg_from_oldAMF.txt"
udm_pathd4 = "D:\Testcase\Locker\Attach\CN\-UDM\msg_from_SMF.txt"
smf_pathd1 = "D:\Testcase\Locker\Attach\CN\SMF\msg_from_newAMF.txt"
smf_pathd2 = "D:\Testcase\Locker\Attach\CN\SMF\msg_from_UPF.txt"
smf_pathd3 = "D:\Testcase\Locker\Attach\CN\SMF\msg_from_PCF.txt"
smf_pathd4 = "D:\Testcase\Locker\Attach\CN\SMF\msg_from_UDM.txt"
upf_pathd1 = "D:\Testcase\Locker\Attach\CN\-UPF\msg_from_SMF.txt"
pcf_pathd1 = "D:\Testcase\Locker\Attach\CN\PCF\msg_from_newAMF.txt"
pcf_pathd2 = "D:\Testcase\Locker\Attach\CN\PCF\msg_from_SMF.txt"
old_amf_pathd1 = "D:\Testcase\Locker\Attach\CN\Old_AMF\msg_from_newAMF.txt"
new_amf_pathd1 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_AUSF.txt"
new_amf_pathd2 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_EIR.txt"
new_amf_pathd3 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_gNB.txt"
new_amf_pathd4 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_N3IWF.txt"
new_amf_pathd5 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_oldAMF.txt"
new_amf_pathd6 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_PCF.txt"
new_amf_pathd7 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_SMF.txt"
new_amf_pathd8 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_UDM.txt"
new_amf_pathd9 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_UE.txt"
n3iwf_pathd1 = "D:\Testcase\Locker\Attach\CN\-N3IWF\msg_from_newAMF.txt"
eir_pathd1 = "D:\Testcase\Locker\Attach\CN\EIR\msg_from_newAMF.txt"
ausf_pathd1 = "D:\Testcase\Locker\Attach\CN\AUSF\msg_from_newAMF.txt"
ausf_pathd2 = "D:\Testcase\Locker\Attach\CN\AUSF\msg_from_UDM.txt"
smsf_dpath1 = "D:\Testcase\Locker\Attach\CN\SMSF\msg_from_newAMF.txt"
smsf_dpath2 = "D:\Testcase\Locker\Attach\CN\SMSF\msg_from_UDM.txt"
new_amf_pathd10 = "D:\Testcase\Locker\Attach\CN\-New_AMF\msg_from_SMSF.txt"
udm_pathd5 = "D:\Testcase\Locker\Attach\CN\-UDM\msg_from_SMSF.txt"

#Handover paths

hanue_npath = "D:\Testcase\Locker\Handover\-UE"
hanue_spath = "D:\Testcase\Locker\Handover\-UE\msg_from_UE.txt"
hanue_pathd1 = "D:\Testcase\Locker\Handover\-UE\msg_from_SgNB_DU.txt"
hanue_npathd2 = "D:\Testcase\Locker\Handover\-UE\msg_from_TgNB_DU.txt"
hanue_npathd3 = "D:\Testcase\Locker\Handover\-UE\msg_from_TgNB.txt"
hanue_npathd4 = "D:\Testcase\Locker\Handover\-UE\msg_from_SgNB.txt"

Tgnb_npath = "D:\Testcase\Locker\Handover\Target_gNB"
Tgnb_spath = "D:\Testcase\Locker\Handover\Target_gNB\msg_from_TgNB.txt"
Tgnb_pathd1 = "D:\Testcase\Locker\Handover\Target_gNB\msg_from_AMF.txt"
Tgnb_pathd2 = "D:\Testcase\Locker\Handover\Target_gNB\msg_from_UE.txt"
Tgnb_pathd3 = "D:\Testcase\Locker\Handover\Target_gNB\msg_from_SgNB.txt"

Tdu_npath = "D:\Testcase\Locker\Handover\Target_gNB\Target_gNB_DU"
Tdu_spath = "D:\Testcase\Locker\Handover\Target_gNB\Target_gNB_DU\msg_from_TgNB_DU.txt"
Tdu_pathd1 = "D:\Testcase\Locker\Handover\Target_gNB\Target_gNB_DU\msg_from_gNB_CU.txt"
Tdu_pathd2 = "D:\Testcase\Locker\Handover\Target_gNB\Target_gNB_DU\msg_from_UE.txt"

Sgnb_npath = "D:\Testcase\Locker\Handover\Source_gNB"
Sgnb_spath = "D:\Testcase\Locker\Handover\Source_gNB\msg_from_SgNB.txt"
Sgnb_pathd1 = "D:\Testcase\Locker\Handover\Source_gNB\msg_from_AMF.txt"
Sgnb_pathd2 = "D:\Testcase\Locker\Handover\Source_gNB\msg_from_UE.txt"
Sgnb_pathd3 = "D:\Testcase\Locker\Handover\Source_gNB\msg_from_TgNB.txt"
Sgnb_pathd4 = "D:\Testcase\Locker\Handover\Source_gNB\msg_from_SMF.txt"

Sdu_npath = "D:\Testcase\Locker\Handover\Source_gNB\Source_gNB_DU"
Sdu_spath = "D:\Testcase\Locker\Handover\Source_gNB\Source_gNB_DU\msg_from_SgNB_DU.txt"
Sdu_pathd1 = "D:\Testcase\Locker\Handover\Source_gNB\Source_gNB_DU\msg_from_gNB_CU.txt"
Sdu_pathd2 = "D:\Testcase\Locker\Handover\Source_gNB\Source_gNB_DU\msg_from_UE.txt"


gnbcu_npath = "D:\Testcase\Locker\Handover\gNB_CU"
gnbcu_spath = "D:\Testcase\Locker\Handover\gNB_CU\msg_from_gNB_CU.txt"
gnbcu_pathd1 = "D:\Testcase\Locker\Handover\gNB_CU\msg_from_SgNB_DU.txt"
gnbcu_pathd2 = "D:\Testcase\Locker\Handover\gNB_CU\msg_from_TgNB_DU.txt"

amf_npath = "D:\Testcase\Locker\Handover\CN\AMF"
amf_spath = "D:\Testcase\Locker\Handover\CN\AMF\msg_from_AMF.txt"
amf_pathd1 = "D:\Testcase\Locker\Handover\CN\AMF\msg_from_TgNB.txt"
amf_pathd2 = "D:\Testcase\Locker\Handover\CN\AMF\msg_from_SgNB.txt"
amf_pathd3 = "D:\Testcase\Locker\Handover\CN\AMF\msg_from_TSMF.txt"

HO_smf_npath = "D:\Testcase\Locker\Handover\CN\SMF"
HO_smf_spath = "D:\Testcase\Locker\Handover\CN\SMF\msg_from_SMF.txt"
HO_smf_pathd1 = "D:\Testcase\Locker\Handover\CN\SMF\msg_from_AMF.txt"
HO_smf_pathd2 = "D:\Testcase\Locker\Handover\CN\SMF\msg_from_TSMF.txt"
HO_smf_pathd3 = "D:\Testcase\Locker\Handover\CN\SMF\msg_from_TAMF.txt"

HO_Tamf_npath = "D:\Testcase\Locker\Handover\T_CN\T_AMF"
HO_Tamf_spath = "D:\Testcase\Locker\Handover\T_CN\T_AMF\msg_from_TAMF.txt"
HO_Tamf_pathd1 = "D:\Testcase\Locker\Handover\T_CN\T_AMF\msg_from_AMF.txt"
HO_Tamf_pathd2 = "D:\Testcase\Locker\Handover\T_CN\T_AMF\msg_from_TSMF.txt"
HO_Tamf_pathd3 = "D:\Testcase\Locker\Handover\T_CN\T_AMF\msg_from_SMF.txt"

HO_Tsmf_npath = "D:\Testcase\Locker\Handover\T_CN\T_SMF"
HO_Tsmf_spath = "D:\Testcase\Locker\Handover\T_CN\T_SMF\msg_from_TSMF.txt"
HO_Tsmf_pathd1 = "D:\Testcase\Locker\Handover\T_CN\T_SMF\msg_from_TAMF.txt"
HO_Tsmf_pathd2 = "D:\Testcase\Locker\Handover\T_CN\T_SMF\msg_from_SMF.txt"

#RAN Paths

ran_gnb_npath = "D:\Testcase\Locker\RAN\gNB"
ran_gnb_spath = "D:\Testcase\Locker\RAN\gNB\msg_from_gNB.txt"
ran_gnb_pathd1 = "D:\Testcase\Locker\RAN\gNB\msg_from_CU.txt"

cn_npath = "D:\Testcase\Locker\RAN\CN"
cn_spath = "D:\Testcase\Locker\RAN\CN\msg_from_core.txt"
cn_pathd1 = "D:\Testcase\Locker\RAN\CN\msg_from_CU.txt"

cu_npath = "D:\Testcase\Locker\RAN\gNB\CU"
cu_spath = "D:\Testcase\Locker\RAN\gNB\CU\msg_from_CU.txt"
cu_pathd1 = "D:\Testcase\Locker\RAN\gNB\CU\msg_from_DU.txt"
cu_pathd2 = "D:\Testcase\Locker\RAN\gNB\CU\msg_from_core.txt"
cu_pathd3 = "D:\Testcase\Locker\RAN\gNB\CU\msg_from_gNB.txt"

du_npath = "D:\Testcase\Locker\RAN\gNB\DU"
du_spath = "D:\Testcase\Locker\RAN\gNB\DU\msg_from_DU.txt"
du_pathd1 = "D:\Testcase\Locker\RAN\gNB\DU\msg_from_CU.txt"




