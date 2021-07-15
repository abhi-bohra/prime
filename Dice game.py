#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random      
   
def diceNumber():
    
    n = input("press enter to roll the dice ")
      
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
      
    return (d1, d2)  
  
def twoDice(total):
    d1, d2 = total
    print("Sum of numbers you have got are {} + {} = {}".format(d1, d2, sum(total)))

value = diceNumber()
twoDice(value)
  
sum_of_dices = sum(value)
  
if sum_of_dices in (7, 11):
    result = "you won"
elif sum_of_dices in (2, 3, 12):
    result = "you lost"
       
else:  
    result = "continue"
    currentpoint = sum_of_dices
    print("your current point is", currentpoint)
    
while result == "continue":
    value = diceNumber()
    twoDice(value)
    sum_of_dices = sum(value)
      
    if sum_of_dices == currentpoint:
        result = "you won"
          
    elif sum_of_dices == 7:
        result = "you lost"

if result == "you won":
    print("you won")
      
else:
    print("you lost")


# In[ ]:




