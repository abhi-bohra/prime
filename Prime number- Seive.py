#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
class Prime:
    def __init__(self, n):
        self.n = n
    
    def isprime(self):
        primes = []
        for i in range(2,self.n+1):
            primes.append(i)
    
        for j in range(2,int(math.sqrt(self.n))):
            for k in range(j*2, self.n+1, j):
                if k not in primes:
                    continue
                #print(primes)
                #print(k)
                primes.remove(k)
       
        print('Prime numbers are:', primes)
    
p1 = Prime(int(input('Enter a number:')))
p1.isprime()


# In[ ]:




