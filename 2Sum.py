#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        
    def Twosum(self):
        l3 = []
        carry_f = 0
        for i,j in zip(self.l1, self.l2):
            if i + j >= 10:
                l3.append((i+j)%10)
                carry_f = 1
                    
            else:
                l3.append(i+j+carry_f)
        print(l3) 
                    
p1 = Solution(l1 = [4,5,6], l2 = [2,5,3])
p1.Twosum()
my list= []

