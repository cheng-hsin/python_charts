def list_aggregator(a_list, operation):
    x=0
    if operation == 'add':
        for i in range(4):
            x=x+a_list[i]
        return x
    if operation == 'multiply':
        x=1
        for i in range(4):
            x=x*a_list[i]
        return x  
   
print(list_aggregator([5, 5, 6, 6],'add'))
print(list_aggregator([-5, -5, -6, 6],'multiply'))
