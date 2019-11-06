import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")
    
    download_num=int(input("請問要下載的數量: "))
    
    photo_list =m.get_photolist(photo_name, download_num)
    
    
    if photo_list == None:
        print("找不到圖片,換個關鍵字")
        
    else:
        if len(photo_list) < download_num:
            print("相關圖片僅有",len(photo_list),"張")
        
        else:
            print("取得所有圖片連結")
        
        break
    
print("開始下載...")
    
for i in range(len(photo_list)):
    m.download_pic(photo_list[i] , str(i+1)) #數字編號為檔名
        
print("\n下載完畢")
    
