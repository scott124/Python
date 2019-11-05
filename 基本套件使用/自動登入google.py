from selenium import webdriver
from time import sleep

opt=webdriver.ChromeOptions()

opt.add_experimental_option('prefs',{'profile.default_content_setting_values':
                                     {'notifications':2}})#加入 禁止顯示訊息框 選項

    
browser=webdriver.Chrome(options =opt)  #以options 建立瀏覽器物件
browser.get('http://www.google.com')
browser.maximize_window()
browser.find_element_by_id('gb_70').click()

browser.find_element_by_id('identifierId').send_keys('scott09171202')
browser.find_element_by_id('identifierNext').click()
sleep(3)

browser.find_element_by_name('password').send_keys('s0927012')
browser.find_element_by_id('passwordNext').click()