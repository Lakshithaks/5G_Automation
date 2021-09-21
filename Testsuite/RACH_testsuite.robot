*** Settings ***

Library    os
Resource   ${EXECDIR}/Res/Attach_Keyword.robot
Variables  ${EXECDIR}/Variablefile/config_file.py
Library    ${EXECDIR}/Lib/attach_function.py


*** Test Cases ***

TC_attach_1.0: UL synchronization
#    Unlock A Window Folder
    Copying Reqfile To Gnb
    Request Validation
    Copying Resfile To Ue
    Response Validation

TC_attach_1.0: Delete messages
    Deleting Printed Messages
    Request Validation
    Response Validation
#    Lock A Window Folder
