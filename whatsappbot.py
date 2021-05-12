from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time


chrome = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)


chrome.get("https://web.whatsapp.com")
time.sleep(7)

search_box = chrome.find_element_by_class_name("_2_1wd")
search_box.send_keys("test")
search_box.send_keys(Keys.ENTER)

message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys("Hello!!")
message_box.send_keys(Keys.ENTER)

for i in range(0,10):
    message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys("Sorry to disturb you Mr.busyyyy:)")
    message_box.send_keys(Keys.ENTER)

emoji = [":-)",";-)",">_<",":-(","^_^"]    

for i in range(0,2):
    message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys(random.choice(emoji))
    message_box.send_keys(Keys.ENTER)
