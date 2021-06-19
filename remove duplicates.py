#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def remove():
    n = len(l)
    
    for i in l:
        if i not in x:
            x.append(i)
            
l = [4,6,8,2,4,6]
x = []
remove()
print(x)  

