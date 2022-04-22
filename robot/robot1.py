import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.find_element(By.TAG_NAME,"button")
# Necessary webdrivers ned to be imported


# Lets open google.com in the first tab
driver.get("file:///home/mohamed/Bureau/test_entretien/c/robot_framwork/image/robot_canada/r14/robot14.html")
#driver.navigate().to("https://www.google.com/") exist in selenuim but not exist in in selenuim with java
driver.maximize_window()
time.sleep(15)