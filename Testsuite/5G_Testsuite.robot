"""
Author: Priyanka and Lakshitha
How to execute testcase: robot -t "test case name" -d Report Testsuite/5G_Testsuite.robot
"""

*** Settings ***

Library    os
Resource   ${EXECDIR}/Res/5G_keyword.robot
Variables  ${EXECDIR}/VariableFiles/config_file.py
Library    ${EXECDIR}/Lib/attach_function.py
Library    ${EXECDIR}/Lib/attach1.py
Library    ${EXECDIR}/Lib/handover.py
Library    ${EXECDIR}/Lib/Ran.py


*** Test Cases ***
TC_attach_1.1: Registration procedure
    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Registration Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.2: UL synchronization
    Lock A Window Folder
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    Rach Validation
    Deleting Printed Messages
    Rach Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.3: Initial registration with correct HNI

    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Reg Correct HNI Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.4: Initial registration with incorrect HNI

    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Reg With Incorrect HNI Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.5: Combined EPS and IMSI Attach

    Lock A Window Folder
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    EPS Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.6: Initial registration from aeroplane mode to normal mode
    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Aeroplane Mode To Normal Mode Val
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.9: Registration Reject with incorrect APN

    Lock A Window Folder
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    APN Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.10: Bearer context setup over F1-U
    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Bearer Setup Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.11: Bearer context release over F1-U
    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Bearer Release Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.13: Uplink and Downlink
    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Bearer Setup Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.14: SRB1 setup procedure
    Lock A Window Folder
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    SRB1 Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.15: Ue Initiated Deregistration procedure

    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Deregistration Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.16: Initial Registration when cell is barred

    Lock A Window Folder
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    Cell Barred Validatiom
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.17: MIB SIB decoding for SSB case C

    Lock A Window Folder
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    MIB And SIB Decode
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.31: Network Initiated Deregistration procedure

    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Network Initiated Dereg Val
    Lock A Window Folder
    Unlock A Window Folder

TC_attach_1.32: Registration procedures for SMS over NAS

    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Reg For SMS Over NAS
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.1: Handover Procedures

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    Handover Prepration Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.2: Xn based inter NG-RAN Handover

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    Xn Based Inter RAN Handover Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.3: Inter NG-RAN N2 handover

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    Inter NG-RAN N2 handover Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.5: FDD intra frequency Handover in FR1 bands

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    FDD Intra Frequency Handover Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.6: FDD inter frequency Handover in FR1 bands

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    FDD Inter Frequency Handover Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.7: TDD intra frequency Handover in FR1 bands

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    TDD Intra Frequency Handover Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.8: TDD inter frequency Handover in FR1 bands

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    TDD Inter Frequency Handover Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.22: Handover counters

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    Handover Counter Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.29: Inter-NR Mobility

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    Inter NR Mobility Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_HO_1.30: Intra-NR Mobility

    Lock A Window Folder
    Unlock A Window Folder
    Source To Destination In Handover
    Intra NR Mobility Validation
    Lock A Window Folder
    Unlock A Window Folder

#RAN
TC_F1_1.1: F1 Setup and NG Setup to activate cell in gNB-DU

    Unlock A Window Folder
    Source To Destination In RAN
    F1 and NG Setup in gNB-DU Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.2: F1 Setup Procedure Failure Operations

    Unlock A Window Folder
    Source To Destination In RAN
    F1 Setup Procedure Failure Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.3: F1 Setup Removal Procedure gNB DU Request Successfully Operations

    Unlock A Window Folder
    Source To Destination In RAN
    F1 Setup Removal(gNB DU) Successful Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.4: F1 Setup Removal Procedure gNB DU Request Failure Operations

    Unlock A Window Folder
    Source To Destination In RAN
    F1 Setup Removal(gNB DU) Failure Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.5: F1 Setup Removal Procedure gNB CU Request Successfully Operations

    Unlock A Window Folder
    Source To Destination In RAN
    F1 Setup Removal(gNB CU) Successful Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.6: F1 Setup Removal Procedure gNB CU Request Failure Operations

    Unlock A Window Folder
    Source To Destination In RAN
    F1 Setup Removal(gNB CU) Failure Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.7: GNB-DU Configuration Update Procedure Successful operation

    Unlock A Window Folder
    Source To Destination In RAN
    GNB-DU Configuration Update Successful Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.8: GNB-DU Configuration Update Procedure Failure operation

    Unlock A Window Folder
    Source To Destination In RAN
    GNB-DU Configuration Update Failure Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.9: GNB-CU Configuration Update Procedure Successful operation

    Unlock A Window Folder
    Source To Destination In RAN
    GNB-CU Configuration Update Successful Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.10: GNB-CU Configuration Update Procedure Failure operation

    Unlock A Window Folder
    Source To Destination In RAN
    GNB-CU Configuration Update Failure Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.11: UE context setup success procedure

    Unlock A Window Folder
    Source To Destination In RAN
    UE Context Setup Success Validation
    Lock A Window Folder
    Unlock A Window Folder

TC_F1_1.12: UE context setup failure procedure

    Unlock A Window Folder
    Source To Destination In RAN
    UE Context Setup Failure Validation
    Lock A Window Folder
    Unlock A Window Folder


TC_F1_1.13: UE context release request gnb-du intiated

    Unlock A Window Folder
    UE Context release (DU) validation
    Lock A Window Folder
    Unlock A Window Folder



