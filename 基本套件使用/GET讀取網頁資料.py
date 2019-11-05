import requests

jojo=requests.get('http://www.flag.com.tw') #向網站發出GET請求,並將回應物件儲存到r

if jojo.status_code == 200:                 #如果是200表示OK
    print(jojo.text)                        #將回應文字(Sorce code)印出來

else:
    print(jojo.status_code, jojo.reason)       #不是的話印出 狀態碼及錯誤原因