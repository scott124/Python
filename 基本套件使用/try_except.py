while True:
    s=input('輸入100的餘數:')
    try:
        i=100/float(s)
        print('100除',s,'=',i)
        break
    except ValueError as e:             #捕捉職錯誤的例外,並將例外存到e
        print('發生 ValueError 例外:','e')
    
    except ZeroDivisionError:           #捕捉除以0的例外,省略as
        print('發生ZeroDivisionError例外')
    except:
        print('其它例外')
    print('進入下一迴圈')
print('程式正常57結束')