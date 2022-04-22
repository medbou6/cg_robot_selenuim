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
time.sleep(5)
# Lets open https://www.bing.com/ in the second tab
driver.execute_script("window.open('about:blank','secondtab')")
driver.switch_to.window("secondtab")
driver.get('https://www.bing.com/')
time.sleep(5)
# Lets open https://www.facebook.com/ in the third tab
driver.execute_script("window.open('about:blank','thirdtab')")
driver.switch_to.window("thirdtab")
driver.get("file:///home/mohamed/Bureau/test_entretien/coding_game/selenuim/image/q8/q8.html")
time.sleep(5)

#driver.close() #close the only curent window
#driver.quit() #close all the window opened
time.sleep(5)
true_respance=input.get_attribute("value")
print(true_respance)



'''
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
'''