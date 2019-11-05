import twstock

stock=twstock.Stock('2330')
print('日期:',stock.date[-1]) #輸出近一日資料
print('開盤價',stock.open[-1])
print('最高價',stock.high[-1])
print('最低價',stock.low[-1])
print('漲跌價差:',stock.change[-1])
print('成交筆數',stock.transaction[-1])
print('總成交股數',stock.capacity[-1])
print('總成交金額',stock.turnover[-1])

print('收盤價:',stock.price) #越後面資料越新


print('\n',stock.moving_average(stock.price,5)) #計算每天的五日移動平均收盤價

bfp=twstock.BestFourPoint(stock)    #以stock建立四大買賣點物件
print(bfp.best_four_point())        #判斷是否為四大買賣點,如果是澤回傳true

#四大賣點:  1.量大收紅 2.量縮價不跌 3.三日均價由下往上(由上往下) 4.三日均價大於(小於)六日均價



