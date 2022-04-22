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
driver.get("file:///home/mohamed/Bureau/test_entretien/coding_game/selenuim/image/q8/q8.html")
time.sleep(10)
input = driver.find_element(By.ID,"firstName")
#print(len(my_link))

#input.send_keys("mmmmmm")
text=input.get_attribute("innerText")
text2=input.text
print(text)
print(text2)
true_respance=input.get_attribute("value")
print(true_respance)