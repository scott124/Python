import twstock

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
        
name,price=get_price('2330')

act,why=get_best('2330')

print(name,price,act,why,sep=' | ')