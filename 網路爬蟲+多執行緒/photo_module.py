import requests
from bs4 import BeautifulSoup


  
def download_pic(url,path):
    
    pic=requests.get(url)
    
    path+=url[url.rfind('.'):]  #路徑加上圖片附檔名   r=rear 從字尾找
    
    
    f=open(pic_path,'wb')       #已指定路徑建立檔案  b=binary w=write
    f.write(pic.content)        #將HTTP Response物件的content寫入檔案中
    f.close()
    
    return f

pic_path="download"            #設定圖片儲存名稱和路徑




  
def get_photolist(photo_name,download_num):
    page = 1            #初始頁數
    photo_list= []      #建立空的圖片list
    
    while True:
        url='https://pixabay.com/zh/images/search/'+photo_name+ '/?pagi=' + str(page)      
        #設定連結
        
        html=requests.get(url)
        html.encoding='utf-8'
        
        bs=BeautifulSoup(html.text,'lxml')  #解析網頁
        
        photo_item=bs.find_all('div', {'class':'item'}) #尋找所有標籤為div,class為'item'元素
        
        if len(photo_item) == 0:
            return None
        
        for i in range(len(photo_item)):
            photo=photo_item[i].find('img')['src']      #尋找'img'並取出src之內容
            
            if photo in photo_list:
                return photo_list
            
            if photo == '/static/img/blank.gif':
                photo = photo_item[i].find('img')['data-lazy'] #如果連結為空白,則尋找標籤img中data-lazy中的內容
                
            photo_list.append(photo)                    #將找到的連結新進list中
            if len(photo_list) >= download_num:
                return photo_list                       #如果圖片連結已達指定數量,則回傳list
    
        page+=1
