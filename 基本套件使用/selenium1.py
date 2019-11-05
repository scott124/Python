from selenium import webdriver             #匯入selenium的driver
from time import sleep                     #匯入內建time模組的sleep()函式

browser=webdriver.Chrome()                 #建立chrome瀏覽器物件
browser.get('http://www.google.com.tw')

print('標題:'+browser.title)                  
print('網址:'+browser.current_url)            
print('內容:'+browser.page_source[0:50])     #輸出網頁原始碼前50個字
print('視窗:',browser.get_window_rect())     #輸出視窗的位置及寬高
browser.save_screenshot('d:/python/123.png')#screenshot
sleep(3)
browser.set_window_rect(1000,500,500,1000)    #改變視窗位置大小
sleep(3)
browser.fullscreen_window()
sleep(3)
browser.quit()
