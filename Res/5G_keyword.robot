"""
Author: Priyanka and Lakshitha
How to execute testcase: robot -t "test case name" -d Report Testsuite/5G_Testsuite.robot
"""

*** Settings ***


*** Keywords ***

Unlock A Window Folder
    unlock

Moving Source Files To Destination Folder
    copy_gnb_ue

Rach Validation
    rach_val

EPS Validation
    eps_val

APN Validation
    apn_val

Deleting Printed Messages
    delete

Lock A Window Folder
    lock

Copying Source Files To Destination Folder
    copy_file

Registration Validation
    int_reg_val

Bearer Setup Validation
    b_setup_val

Bearer Release Validation
    b_release_val

SRB1 Validation
    srb_val

Cell Barred Validatiom
    barred_val

Reg Correct HNI Validation
    crct_hni_val

Reg With Incorrect HNI Validation
    incrct_hni_val

Aeroplane Mode To Normal Mode Val
    AM_to_NM

Deregistration Validation
    dereg_val

Network Initiated Dereg Val
    net_dereg_val

Reg For SMS Over NAS
    reg_sms_nas

MIB And SIB Decode
    mib_sib

#Handover

Source To Destination In Handover
    sour_des

Inter NR Mobility Validation
    inter_nr_mobility

Handover Prepration Validation
    HO_prepration

Xn Based Inter RAN Handover Validation
    Xn_inter_HO

Intra NR Mobility Validation
    intra_nr_mobility

Handover Counter Validation
    HO_counters

Inter NG-RAN N2 handover Validation
    N2_inter_HO

FDD Intra Frequency Handover Validation
    FDD_intra_frequency_Handover

FDD Inter Frequency Handover Validation
    FDD_inter_frequency_Handover

TDD Intra Frequency Handover Validation
    TDD_intra_frequency_Handover

TDD Inter Frequency Handover Validation
    TDD_inter_frequency_Handover

#RAN

Source To Destination In RAN
    mov_ran_files

F1 and NG Setup in gNB-DU Validation
    F1_NG_Setup

F1 Setup Procedure Failure Validation
    F1_Set_Fail

F1 Setup Removal(gNB DU) Successful Validation
    F1_Set_DU_Removal_Suc

F1 Setup Removal(gNB DU) Failure Validation
    F1_Set_DU_Removal_Fail

F1 Setup Removal(gNB CU) Successful Validation
    F1_Set_CU_Removal_Suc

F1 Setup Removal(gNB CU) Failure Validation
    F1_Set_CU_Removal_Fail

GNB-DU Configuration Update Successful Validation
    DU_Con_Update_Suc

GNB-DU Configuration Update Failure Validation
    DU_Con_Update_Fail

GNB-CU Configuration Update Successful Validation
    CU_Con_Update_Suc

GNB-CU Configuration Update Failure Validation
    CU_Con_Update_Fail

UE Context Setup Success Validation
    UE_con_setup_success

UE Context Setup Failure Validation
    UE_con_setup_failure

UE Context release (DU) validation
    UE_context_release_request_DU_intiated
    mov_ran_files
    UE_con_rel_DU

UE Context release (CU) validation
    UE_context_release_request_CU_intiated
    mov_ran_files
    UE_con_rel_CU
