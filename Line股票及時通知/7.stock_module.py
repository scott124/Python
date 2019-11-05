import requests
import twstock

def send_ifttt(v1,v2,v3):        #定義函式向ifttt發送HTTP要求

    url=('https://maker.ifttt.com/trigger/toline/with/'+
         'key/lxAoMuJ8yPBz_Uazf2PzvsmDsoKPWJjJzJbEhBOOgOx'+
         '?value1='+str(v1)+
         '&value2='+str(v2)+
         '&value3='+str(v3))
    
    r=requests.get(url)          #送出HTTP GET並取得網站回應資料
    
    if r.text[:5] == 'Congr':   #回應文字若以 Congr開頭就表示成功了
        print('已傳送(' +str(v1)+', '+str(v2)+', '+str(v3)+ ') 到Line')
        
    return r.text

def get_setting():
    res=[]
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



def get_price(stockid):
    rt=twstock.realtime.get(stockid)
    if rt['success']:
        return (rt['info']['name'],
                float(rt['realtime']['latest_trade_price']))
    
    else:
        return (False,False)

def get_best(stockid):  #檢查是否符合四大賣點
    stock=twstock.Stock(stockid)
    bp=twstock.BestFourPoint(stock).best_four_point()
    
    if(bp):
        return('買進' if bp[0] else '賣出',bp[1]) #傳回買進或賣出的建議
        
    else:
        return(False,False) #都不符合