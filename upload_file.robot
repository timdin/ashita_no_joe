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
    
    ${result} =  api get  ${url}
    Log to console  ${result}
    Log  ${result}
    Should be equal  ${expected}  ${result}