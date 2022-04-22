*** Settings ***
Documentation     Robot to enter weekly sales data into the RobotSpareBin Industries Intranet.
Library           RPA.Browser.Selenium

*** Variables ***
${URL}=    https://robotsparebinindustries.com/

*** Keywords ***
Open The Intranet Website
    Open Available Browser    ${URL}

*** Keywords ***
Log In
    Input Text    username    maria
    Input Password    password    thoushallnotpass
    Submit Form

*** Tasks ***
Open the intranet site and log in
    Open The Intranet Website
    Log In