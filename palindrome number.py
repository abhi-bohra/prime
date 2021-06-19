#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def __init__(self, num):
        self.num = num
                
    def reverse(self):
        y = self.num
        x = 0
        while y != 0:
            r = y % 10
            x = x * 10 + r
            y = y//10
            #print(x)
        if self.num == x:
            return True
        else:
            return False

p1 = Solution(int(input('Enter a number:')))
p1.reverse()


# In[ ]:




