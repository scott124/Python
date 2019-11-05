f=open('a.txt','w',encoding='utf-8')    #以寫入模式,utf-8開啟檔案

f.write('''白日依山盡
黃河入海流
欲窮千里目
更上一層樓''')

f.close()
f=open('a.txt','r',encoding='UTF-8')    #以讀取模式,UTF-8編碼開啟檔案

s=f.readlines()
print(s)
f.close()