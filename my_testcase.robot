*** Settings ***
Library           Selenium2Library


*** Variables ***
${Username}       swtestacademy@gmail.
${Password}       wrongpass
${Browser}         '/home/mohamed/Bureau/test_entretien/chromedriver'
${SiteUrl}        http://www.linkedin.com
${DashboardTitle}    World’s Largest Professional Network | LinkedIn
${ExpectedWarningMessage}    Hmm, we don't recognize that email. Please try again.
${WarningMessage}    Login Failed!
${Delay}          5s
*** Test Cases ***
Login Should Failed With Unregistered Mail Adress
    Open LinkedinPage

*** Keywords ***

Open LinkedinPage
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window



