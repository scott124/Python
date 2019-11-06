import requests

def download_pic(url,path):
    
    pic=requests.get(url)
    
    path+=url[url.rfind('.'):]  #路徑加上圖片附檔名   r=rear 從字尾找
    
    f=open(pic_path,'wb')       #已指定路徑建立檔案  b=binary w=write
    f.write(pic.content)        #將HTTP Response物件的content寫入檔案中
    f.close()


pic_path="download"            #設定圖片儲存名稱和路徑

download_pic(url,pic_path)   