from selenium.webdriver import Chrome
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.geeksforgeeks.org/python-selenium-find-button-by-text/")
'''
#driver = Chrome(executable_path="/home/mohamed/Bureau/test_entretien/chromedriver.exe")

import time



#driver=webdriver.chrome("/home/mohamed/Bureau/test_entretien/chromedriver.exe")
#driver.get("https://www.geeksforgeeks.org/python-selenium-find-button-by-text/")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get("file:///home/mohamed/Bureau/test_entretien/coding_game/selenuim/image/q5/chrome_1.html")
driver.manage().timeouts().implicitlyWait(2,4)
time.sleep(10)
my_link = driver.find_element(By.ID,"shoppingList")
#print(len(my_link))
my_links = driver.find_elements(By.CSS_SELECTOR,"li.item")
print(len(my_links))
#print(len(my_link))
my_links_2 = driver.find_elements(By.CSS_SELECTOR,"li.bought")
print(my_links_2)
print(len(my_links_2))