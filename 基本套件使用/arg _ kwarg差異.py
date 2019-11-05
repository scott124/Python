def price(name,*args,**kwargs):
    print(name,args,':',kwargs,sep=' ')

discount=('早餐8折','消夜9折 ')
drink={'紅茶':40,'咖啡':70,'果汁':85}
price('飲料',*discount,**drink)

#   *arg會打包成tuple
#   **kwarg會打包成dict 