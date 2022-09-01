#https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
from collections import Counter

x = [1, 2,2, 3, 4, 5, 5]

def mode(x):
    
    n = len(x) 
  
    data = Counter(x) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
    if len(mode) == n: 
        get_mode = "No mode found"
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
    print(get_mode) 

    

mode(x)
