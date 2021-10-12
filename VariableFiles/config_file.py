
message_1 = "Random access preamble message - msg1"
message_2 = "Random access response report - msg2\n"
message_3 = "UE identification msg report - msg3"
message_4 = "Contention resolution message report - msg4"
message_5 = "Attach Request:EPS attach type(IE)- Combined EPS/IMSI Attach"
message_6 = "Attach accept:EPS attach Result(IE)- Combined EPS/IMSI Attach"
message_7 = "PDN connectivity request:IE - APN(XXX)"
message_8 = "PDN connectivity Reject:IE- ESM cause #27 (missing or unknown APN)"
message_9 = "BEARER CONTEXT MODIFICATION REQUEST"
message_10 = "BEARER CONTEXT MODIFICATION RESPONSE\n"
message_11 = "F1 UE context modification procedure"
message_12 = "UE Context Release"
message_13 = "BEARER CONTEXT RELEASE COMMAND"
message_14 = "F1 UE context release procedure"
message_15 = "BEARER CONTEXT RELEASE COMPLETE"
message_16 = "BEARER CONTEXT SETUP REQUEST:IE - UL TNL address information for S1-U or NG-U\n"
message_17 = "BEARER CONTEXT SETUP RESPONSE\n"
message_18 = "F1 UE context setup procedure"
message_19 = "RRCSetupRequest:establishmentCause-highPriorityAccess\n"
message_20 = "RRCConnectionSetup"
message_21 = "RRCConnectionSetupComplete"
message_22 = "Registration Request"
message_23 = "Registration Reject:Cause(IE)-Cell barred"
message_24 = "Namf_Communication_UEContextTransfer request"
message_25 = "Namf_Communication_UEContextTransfer response"
message_26 = "Identity Request\n"
message_27 = "Identity Response\n"
message_28 = "Nausf_UEAuthenticate_authenticate Request\n"
message_29 = "Nudm_UEAuthenticate_Get Request - IE: SUCI(correct)\n"
message_30 = "Nudm_UEAuthenticate_Get Response\n"
message_31 = "Nausf_UEAuthentication_authenticate Response - IE: SUPI(correct)\n"
message_32 = "NAS Authentication Request\n"
message_33 = "NAS Authentication Response\n"
message_34 = "NAS Security Mode Command\n"
message_35 = "NAS Security Mode Complete\n"
message_36 = "N5g-eir_EquipmentIdentityCheck_Request"
message_37 = "N5g-eir_EquipmentIdentityCheck_Response"
message_38 = "Nudm_UECM_Registration Request"
message_39 = "Nudm_UECM_Registration Response"
message_40 = "Nudm_SubscriberDataManagement_Get Request"
message_41 = "Nudm_SubscriberDataManagement_Get Response"
message_42 = "Nudm_UEContextManagement_Deregistration_Notify"
message_43 = "Npcf_AMPolicyControl_Create Request"
message_44 = "Npcf_AMPolicyControl_Create Response"
message_45 = "Nsmf_PDUSession_UpdateSMContext Request"
message_46 = "Nsmf_PDUSession_UpdateSMContext Response"
message_47 = "N2 AMF Mobility Request"
message_48 = "N2 AMF Mobility Response"
message_49 = "Registration Accept"
message_50 = "Registration Complete"
message_51 = "Nudm_SDM_Info"
message_52 = "Nudm_UEAuthenticate_Get Request - IE: SUCI(incorrect)"
message_53 = "Deregistration Request-IE:(5G-GUTI, Deregistration type (e.g. Switch off), Access Type)"
message_54 = "Nsmf_PDUSession_ReleaseSMContext Request"
message_55 = "N4 Session Release Request"
message_56 = "N4 Session Release Response"
message_57 = "Nsmf_PDUSession_ReleaseSMContext Response"
message_58 = "SM Policy Association Termination"
message_59 = "Nudm_SDM_Unsubscribe"
message_60 = "Nudm_UECM_Deregistration"
message_61 = "AMF-initiated AM Policy Association Termination"
message_62 = "AMFinitiated UE Policy Association Termination"
message_63 = "De-registration Accept"
message_64 = "Signalling Connection Release"


 # path for locker

dir_path = "D:\TestCases"
loc_path = "D:\TestCases\Locker"

#paths for gnb & ue
path1 = "D:\TestCases\Locker\Attach\Attach\-UE\msg_from_UE.txt"
path2 = "D:\TestCases\Locker\Attach\gNB\msg_from_gNB.txt"
path3 = "D:\TestCases\Locker\Attach\gNB\msg_from_UE.txt"
path4 = "D:\TestCases\Locker\Attach\-UE\msg_from_gNB.txt"
gnb_npath = "D:\TestCases\Locker\Attach\gNB"
ue_npath = "D:\TestCases\Locker\Attach\-UE"
ue_pathd1 = "D:\TestCases\Locker\Attach\-UE\msg_from_newAMF.txt"
gnb_pathd1 = "D:\TestCases\Locker\Attach\gNB\msg_from_newAMF.txt"

#password for locker
pw = "password"
pw1 = "password"

#path for cu,du & menb
cp_path = "D:\TestCases\Locker\Attach\gNB\CU-CP\msg_from_CUCP.txt"
cp1_path = "D:\TestCases\Locker\Attach\gNB\CU-CP"
cp2_path = "D:\TestCases\Locker\Attach\gNB\CU-CP\msg_from_CUUP.txt"
cp3_path = "D:\TestCases\Locker\Attach\gNB\CU-CP\msg_from_DU.txt"
cp4_path = "D:\TestCases\Locker\Attach\gNB\CU-CP\msg_from_Menb.txt"
up_path = "D:\TestCases\Locker\Attach\gNB\CU-UP\msg_from_CUUP.txt"
up1_path = "D:\TestCases\Locker\Attach\gNB\CU-UP"
up2_path = "D:\TestCases\Locker\Attach\gNB\CU-UP\msg_from_CUCP.txt"
du_path = "D:\TestCases\Locker\Attach\gNB\DU\msg_from_DU.txt"
du1_path = "D:\TestCases\Locker\Attach\gNB\DU"
du2_path = "D:\TestCases\Locker\Attach\gNB\DU\msg_from_CUCP.txt"
me_path = "D:\TestCases\Locker\Attach\MeNB\msg_from_Menb.txt"
me1_path = "D:\TestCases\Locker\Attach\MeNB"

#path for core compoents
ausf_npath = "D:\TestCases\Locker\Attach\CN\AUSF"
ausf_spath = "D:\TestCases\Locker\Attach\CN\AUSF\msg_from_AUSF.txt"
eir_npath = "D:\TestCases\Locker\Attach\CN\EIR"
eir_spath = "D:\TestCases\Locker\Attach\CN\EIR\msg_from_EIR.txt"
n3iwf_npath = "D:\TestCases\Locker\Attach\CN\-N3IWF"
n3iwf_spath = "D:\TestCases\Locker\Attach\CN\-N3IWF\msg_from_N3IWF.txt"
new_amf_npath = "D:\TestCases\Locker\Attach\CN\-New_AMF"
new_amf_spath = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_newAMF.txt"
old_amf_npath = "D:\TestCases\Locker\Attach\CN\Old_AMF"
old_amf_spath = "D:\TestCases\Locker\Attach\CN\Old_AMF\msg_from_oldAMF.txt"
pcf_npath = "D:\TestCases\Locker\Attach\CN\PCF"
pcf_spath = "D:\TestCases\Locker\Attach\CN\PCF\msg_from_PCF.txt"
smf_npath = "D:\TestCases\Locker\Attach\CN\SMF"
smf_spath = "D:\TestCases\Locker\Attach\CN\SMF\msg_from_SMF.txt"
udm_npath = "D:\TestCases\Locker\Attach\CN\-UDM"
udm_spath = "D:\TestCases\Locker\Attach\CN\-UDM\msg_from_UDM.txt"
upf_npath = "D:\TestCases\Locker\Attach\CN\-UPF"
upf_spath = "D:\TestCases\Locker\Attach\CN\-UPF\msg_from_UPF.txt"
smsf_npath = "D:\TestCases\Locker\Attach\CN\SMSF"
smsf_spath = "D:\TestCases\Locker\Attach\CN\SMSF\msg_from_SMSF.txt"

#core validation paths
udm_pathd1 = "D:\TestCases\Locker\Attach\CN\-UDM\msg_from_AUSF.txt"
udm_pathd2 = "D:\TestCases\Locker\Attach\CN\-UDM\msg_from_newAMF.txt"
udm_pathd3 = "D:\TestCases\Locker\Attach\CN\-UDM\msg_from_oldAMF.txt"
udm_pathd4 = "D:\TestCases\Locker\Attach\CN\-UDM\msg_from_SMF.txt"
smf_pathd1 = "D:\TestCases\Locker\Attach\CN\SMF\msg_from_newAMF.txt"
smf_pathd2 = "D:\TestCases\Locker\Attach\CN\SMF\msg_from_UPF.txt"
smf_pathd3 = "D:\TestCases\Locker\Attach\CN\SMF\msg_from_PCF.txt"
smf_pathd4 = "D:\TestCases\Locker\Attach\CN\SMF\msg_from_UDM.txt"
upf_pathd1 = "D:\TestCases\Locker\Attach\CN\-UPF\msg_from_SMF.txt"
pcf_pathd1 = "D:\TestCases\Locker\Attach\CN\PCF\msg_from_newAMF.txt"
pcf_pathd2 = "D:\TestCases\Locker\Attach\CN\PCF\msg_from_SMF.txt"
old_amf_pathd1 = "D:\TestCases\Locker\Attach\CN\Old_AMF\msg_from_newAMF.txt"
new_amf_pathd1 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_AUSF.txt"
new_amf_pathd2 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_EIR.txt"
new_amf_pathd3 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_gNB.txt"
new_amf_pathd4 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_N3IWF.txt"
new_amf_pathd5 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_oldAMF.txt"
new_amf_pathd6 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_PCF.txt"
new_amf_pathd7 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_SMF.txt"
new_amf_pathd8 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_UDM.txt"
new_amf_pathd9 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_UE.txt"
n3iwf_pathd1 = "D:\TestCases\Locker\Attach\CN\-N3IWF\msg_from_newAMF.txt"
eir_pathd1 = "D:\TestCases\Locker\Attach\CN\EIR\msg_from_newAMF.txt"
ausf_pathd1 = "D:\TestCases\Locker\Attach\CN\AUSF\msg_from_newAMF.txt"
ausf_pathd2 = "D:\TestCases\Locker\Attach\CN\AUSF\msg_from_UDM.txt"
smsf_dpath1 = "D:\TestCases\Locker\Attach\CN\SMSF\msg_from_newAMF.txt"
smsf_dpath2 = "D:\TestCases\Locker\Attach\CN\SMSF\msg_from_UDM.txt"
new_amf_pathd10 = "D:\TestCases\Locker\Attach\CN\-New_AMF\msg_from_SMSF.txt"
udm_pathd5 = "D:\TestCases\Locker\Attach\CN\-UDM\msg_from_SMSF.txt"

#Handover paths

hanue_npath = "D:\TestCases\Locker\Handover\-UE"
hanue_spath = "D:\TestCases\Locker\Handover\-UE\msg_from_UE.txt"
hanue_pathd1 = "D:\TestCases\Locker\Handover\-UE\msg_from_SgNB_DU.txt"
hanue_npathd2 = "D:\TestCases\Locker\Handover\-UE\msg_from_TgNB_DU.txt"


Tdu_npath = "D:\TestCases\Locker\Handover\Target_gNB_DU"
Tdu_spath = "D:\TestCases\Locker\Handover\Target_gNB_DU\msg_from_TgNB_DU.txt"
Tdu_pathd1 = "D:\TestCases\Locker\Handover\Target_gNB_DU\msg_from_gNB_CU.txt"
Tdu_pathd2 = "D:\TestCases\Locker\Handover\Target_gNB_DU\msg_from_UE.txt"

Sdu_npath = "D:\TestCases\Locker\Handover\Source_gNB_DU"
Sdu_spath = "D:\TestCases\Locker\Handover\Source_gNB_DU\msg_from_SgNB_DU.txt"
Sdu_pathd1 = "D:\TestCases\Locker\Handover\Source_gNB_DU\msg_from_gNB_CU.txt"
Sdu_pathd2 = "D:\TestCases\Locker\Handover\Source_gNB_DU\msg_from_UE.txt"

gnbcu_npath = "D:\TestCases\Locker\Handover\gNB_CU"
gnbcu_spath = "D:\TestCases\Locker\Handover\gNB_CU\msg_from_gNB_CU.txt"
gnbcu_pathd1 = "D:\TestCases\Locker\Handover\gNB_CU\msg_from_SgNB_DU.txt"
gnbcu_pathd2 = "D:\TestCases\Locker\Handover\gNB_CU\msg_from_TgNB_DU.txt"
