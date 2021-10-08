*** Settings ***

Library    os
Resource   ${EXECDIR}/Res/attach_keyword.robot
Variables  ${EXECDIR}/VariableFiles/config_file.py
Library    ${EXECDIR}/Lib/attach_function.py
Library    ${EXECDIR}/Lib/attach1.py


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

TC_attach_1.31: Network Initiated Deregistration procedure

    Lock A Window Folder
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Network Initiated Dereg Val
    Lock A Window Folder
    Unlock A Window Folder