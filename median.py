#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Median:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        
    def med(self):
        self.l1.extend(self.l2)
        print(self.l1)
        if len(self.l1)%2 != 0:
            n = len(self.l1)//2
            math.floor(float(n))
            #print(n)
            print(self.l1[n])
            
        else:
            n = len(self.l1)//2
            #print(n)
            print((self.l1[n] + self.l1[n-1])/2)
            
p1 = Median(l1 = [3,5], l2 = [2,6,4,8])
p1.med()


# In[ ]:




