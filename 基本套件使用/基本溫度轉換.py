s=input("Please input temperature:")
if s.count('.')>1:
    
    print('ERROR,Only one point applied')
    
elif s[1:].replace('.','').isdigit(): #判斷除第一字元,其字元去除小數點之後是否均為數字
    
    if s[0] == '-' or s[0].isdigit(): #判斷開頭字元是否為負號或數字
        temp=float(s)
        
        print(f'攝氏{temp}度等於華氏{(temp*9/5)+32:+5.1f} 度')
        print(f'華氏{temp}度等於攝氏{(temp-32)*5/9:+5.1f} 度')
        
    else:
        print("只能以數字or負號開頭")

else:
    print("輸入的溫度無法轉換!")
        
        