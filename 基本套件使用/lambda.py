s=[(3,4),(2,4),(5,3)]

def calAll(rect,func):
    for r in rect:
        print(func(r[0],r[1]),end=' ')
        
calAll(s,lambda w,h:w*h)