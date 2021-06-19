#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def insertion():
    n = len(l)
    for i in range(1,n):
        current = l[i]
        pos = i
        while current < l[pos-1] and pos > 0:
            l[pos] = l[pos-1]
            pos = pos - 1
        l[pos] = current
        print(l)
l = [6,9,7,3,0,1]
insertion()
print(l)

