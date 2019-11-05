from selenium import webdriver
from time import sleep

browser=webdriver.Chrome()

browser.get('http://www.google.com')
print('標題'+browser.title)
browser.set_window_rect(200,100,100,100)
sleep(3006)
browser.quit()