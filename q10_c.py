import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Necessary webdrivers ned to be imported


# Lets open google.com in the first tab
driver.get('http://google.com')
#driver.navigate().to("https://www.google.com/") exist in selenuim but not exist in in selenuim with java
driver.maximize_window()
