import math
x1=eval(input("請輸入x1:"))
x2=eval(input("請輸入x2:"))
y1=eval(input("請輸入y1:"))
y2=eval(input("請輸入y2:"))
print("( "+str(x1)+" , "+str(x2)+" )")
print("( "+str(y1)+" , "+str(y2)+" )")
distance=((x1-x2)**2+(y1-y2)**2)*0.5
print("(x1,x2)到(y1,y2)的距離是",distance)