import random

num = random.randint(1,1000)

answer = -1
start=0
end=1000
while answer != num:
  answer = eval(input('輸入數字1-1000:'))
  
  if answer>num and answer < end:
    print('too big')
    print(str(start)+'~'+str(answer))
    end=answer

  elif answer>num and answer > end:
    print('too big')
    print(str(start)+'~'+str(end))
    
    
  elif answer<num and answer > start:
    print('too small')
    print(str(answer)+'~'+str(end))
    start=answer

  elif answer<num and answer < start:
    print('too small')
    print(str(start)+'~'+str(end))
   
    
  elif num == answer:
    print('bingo!')
