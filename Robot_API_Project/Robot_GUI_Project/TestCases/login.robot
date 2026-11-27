*** Settings ***
Library     SeleniumLibrary
 
*** Variables ***
${url}      http://www.amazon.com/
${browser}      Chrome
 
*** Test Cases***
Verify Login Functionality
    Open browser    ${url}      ${browser}
    Maximize Browser Window
    Sleep       10s
    input Text      id=twotabsearchtextbox       Laptop
    Sleep       10s
    Click Element       id=nav-search-submit-button