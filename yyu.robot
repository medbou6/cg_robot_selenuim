*** Settings ***
Library           Selenium2Library
Documentation        SDSDDDDSD

*** Variables ***
${Username}       swtestacademy@gmail.
${Password}       wrongpass
${Browser}         '/home/mohamed/Bureau/test_entretien/drive2/chromedrive(1)/chromedriver'
${SiteUrl}        http://www.linkedin.com
${DashboardTitle}    World’s Largest Professional Network | LinkedIn
${ExpectedWarningMessage}    Hmm, we don't recognize that email. Please try again.
${WarningMessage}    Login Failed!
${Delay}          5s
*** Test Cases ***
Login Should Failed With Unregistered Mail Adress
    Open LinkedinPage
    Check Title
    Enter User Name
    Enter Wrong Password
    Click Login
    sleep    ${Delay}
    Assert Warning Message
    [Teardown]    Close Browser
*** Keywords ***

Open LinkedinPage
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window
Enter User Name

Enter Wrong Password
    Input Text    id=login-password    ${Password}
Click Login
    Click Button    css=[name=submit]
Check Title
    Title Should be    ${DashboardTitle}
Assert Warning Message
    Element Text Should Be    id=session_key-login-error    ${ExpectedWarningMessage}    ${WarningMessage}

    Input Text    id=login-password    ${Password}
Click Login
    Click Button    css=[name=submit]
Check Title
    Title Should be    ${DashboardTitle}
