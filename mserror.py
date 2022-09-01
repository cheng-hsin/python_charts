def mean_squared_error(y_hat, y):
    mse=0
    for i in range (len(y_hat)):
        mse = mse + ((y_hat[i] - y[i]) ** 2) 


    return mse/5


print(mean_squared_error([1,2,3,4,5],[1,2,3,4,5]))
print(mean_squared_error([1,2,3,4,5],[1,3,5,7,9]))
print(mean_squared_error([1,2,3,4,5],[2,4,6,8,10]))
print(mean_squared_error([1,2,3,4,5],[-1,-2,-3,-4,-5]))
