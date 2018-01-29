***Settings***
Library    place_file.py

***Variables***
${user_name}  yrchen
${password}  Innova_0821
${cid}  VAH60142
${local_path}  C:\Automation\Upload File
***Test Cases***
Test
    [Tags]  Upload File
    [Setup]  ftp login  ${user_name}  ${password}
    ftp place  ${cid}
    [Teardown]  Upload finished

*** Keywords ***
Upload finished
    dissconnect
    move files