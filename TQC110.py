import math
n=eval(input("請輸入n:"))
s=eval(input("請輸入s:"))
area=(n*math.pow(s, 2))/(4*math.tan(math.pi/n))
print("Area = {:.4f}".format(area))