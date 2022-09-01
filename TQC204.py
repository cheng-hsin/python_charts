import operator
num1=eval(input())
num2=eval(input())
op = input()

# operator_dict= {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,
# }

# print(operator_dict[op](num1, num2))

if (op=='+'):
    print(num1+num2)
if (op=='-'):
    print(num1-num2)
if (op=='*'):
    print(num1*num2)



