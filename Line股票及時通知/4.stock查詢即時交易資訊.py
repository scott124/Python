import twstock

rt=twstock.realtime.get('2330') #讀取台積電即時交易資訊

if(rt['success']):  #如果讀取成功
    print(rt)       #輸出字典資訊