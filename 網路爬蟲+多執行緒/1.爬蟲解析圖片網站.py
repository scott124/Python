import requests

from bs4 import BeautifulSoup

url='https://pixabay.com/zh/images/search/%E7%8B%97/'

html=requests.get(url)

html.encoding='utf-8'  #指定編碼

bs=BeautifulSoup(html.text,'lxml')  #解析網頁

photo_item=bs.find_all('div',{'class':'item'}) #尋找所有標籤為div,class為'item'的元素

photo_list= [] #建立空圖片list

for i in range(len(photo_item)):
    
    photo=photo_item[i].find('img')['src']
    photo_list.append(photo)         #將連結新增近list之中
    
print(photo_list)      #顯示圖片list