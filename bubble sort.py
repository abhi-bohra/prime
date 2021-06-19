#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bubble():
    n = len(l)
    for i in range(1,n):
        for j in range(1,n):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
                print(l)
        
l = [6,9,7,3,0,1]
bubble()
print(l)

