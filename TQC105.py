x=eval(input("請輸入分:"))
y=eval(input("請輸入秒:"))
z=eval(input("請輸入公里數:"))
time=x+(y/60)
mile=z/1.6
result=mile/time*60
print("時速"+str(result)+"英哩")