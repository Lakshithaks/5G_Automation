*** Settings ***

Library    os
Resource   ${EXECDIR}/Res/Attach_Keyword.robot
Variables  ${EXECDIR}/Variablefile/config_file.py
Library    ${EXECDIR}/Lib/attach_function.py


*** Test Cases ***

TC_attach_1.2: UL synchronization
#    Unlock A Window Folder
    Copying Reqfile To Gnb
    RACH Request Validation
    Copying Resfile To Ue
    RACH Response Validation

TC_attach_1.2.1: Delete messages
    Deleting Printed Messages
    RACH Request Validation
    RACH Response Validation
#    Lock A Window Folder

TC_attach_1.5: Combined EPS/IMSI attach
#    Unlock A Window Folder
    Copying Reqfile To Gnb
    EPS Request Validation
    Copying Resfile To Ue
    EPS Response Validation
    Deleting Printed Messages
    EPS Request Validation
    EPS Response Validation
