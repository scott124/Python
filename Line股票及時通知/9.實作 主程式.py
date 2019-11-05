import time
import stock_module as m            #自訂模組m

slist=m.get_setting()               #匯入模組中的函式取得股票設定資料

count=len(slist)                    #計算有幾支股票

log1 = []   #紀錄曾經傳送過的股票高或低於期望的訊息，以避免重複傳送
log2 = []   #紀錄曾經傳送過符合四大賣點的訊息，以免重複傳送

for i in range (count):
    log1.append('')
    log2.append('')

check_count=20
while True:
    for i in range(count):              #走訪每一支股票
        id,low,high=slist[i]            #讀出股票的代號、期望買進價格、期望賣出價格
        name,price=m.get_price(id)      #讀取股票名稱喊及時價格
        print('檢查:',name,'股價',price,'區間:',low,'~',high)
        
        if price <= low:
            if log1[i] != '買進':        #再次檢查傳送訊息，以免重複傳送
                m.send_ifttt(name,price,'買進(股價低於 '+str(low)+')')
                log1[i]='買進'           #紀錄傳送訊息，以避免重複傳送
        
        elif price>=high:
            if log1[i] != '賣出':
                m.send_ifttt(name,price,'賣出(股價高於'+str(low)+')')
                log1[i]='賣出'
        
        act,why = m.get_best(id)        #檢查四大賣點
    
        if why:                         #如果符合四大賣點
            if log2[i] !=why:
                m.send_ifttt(name,price,act+'('+why+')')
                log2[i]=why
    
    print('-------------')
    
    check_count-=1      #計數器-1
    
    if check_count ==0: break
    
    time.sleep(180)     #每180 sec 檢查一遍

    
            
            