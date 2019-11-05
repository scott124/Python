from selenium import webdriver
browser=webdriver.Chrome()

browser.get('http://www.facebook.com')

browser.find_element_by_id('email').send_keys('123123')
browser.find_element_by_id('pass').send_keys('456456')
browser.find_element_by_id('loginbutton').click()

