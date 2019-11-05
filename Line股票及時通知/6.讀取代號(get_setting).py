def get_setting():
    res=[]  #準備空序列來讀取及解析結果
    try:
        with open('stock.txt') as f: #用with以讀取模式開啟檔案
            slist=f.readlines()
            print('讀入:',slist)
            for lst in slist:
                s=lst.split(',')    #以','切割為串列
                res.append([s[0].strip(),float(s[1]),float(s[2])])
                
                #append->將結果加到res中
                #strip->去除左右空白
                #float->將股價轉換為float
    except:
        print('stock.txt 讀取錯誤')
    return res

stock=get_setting() #呼叫函式
print('傳回:',stock) #輸出傳回結果