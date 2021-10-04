*** Settings ***

Library    os
Resource   ${EXECDIR}/Res/attach_keyword.robot
Variables  ${EXECDIR}/VariableFiles/config_file.py
Library    ${EXECDIR}/Lib/attach_function.py
Library    ${EXECDIR}/Lib/attach1.py


*** Test Cases ***
TC_attach_1.1: Registration procedure
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Registration Validation
    Lock A Window Folder

TC_attach_1.2: UL synchronization
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    Rach Request Validation
    Rach Response Validation
    Deleting Printed Messages
    Rach Request Validation
    Rach Response Validation
    Lock A Window Folder

TC_attach_1.3: Initial registration with correct HNI

    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Reg Correct HNI Validation
    Lock A Window Folder

TC_attach_1.5: Combined EPS and IMSI Attach
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    EPS Request Validation
    EPS Response Validation
    Deleting Printed Messages
    EPS Request Validation
    EPS Response Validation
    Lock A Window Folder

TC_attach_1.9: Registration Reject with incorrect APN
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    APN Request Validation
    APN Response Validation
    Deleting Printed Messages
    APN Request Validation
    APN Response Validation
    Lock A Window Folder

TC_attach_1.10: Bearer context setup over F1-U
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Bearer Setup Validation
    Lock A Window Folder

TC_attach_1.11: Bearer context release over F1-U
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Bearer Release Validation
    Lock A Window Folder

TC_attach_1.13: Uplink and Downlink
    Unlock A Window Folder
    Copying Source Files To Destination Folder
    Bearer Setup Validation
    Lock A Window Folder

TC_attach_1.14: SRB1 setup procedure
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    SRB1 Validation
    Lock A Window Folder

TC_attach_1.16: Initial Registration when cell is barred
    Unlock A Window Folder
    Moving Source Files To Destination Folder
    Cell Barred Validatiom
    Lock A Window Folder
