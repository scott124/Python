import requests

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

ret =send_ifttt('台積電',99,'建議買進') #傳送HTTP請求到IFTTT
print('IFTTT回應的訊息:',ret)    #輸出IFTTT回應的文字