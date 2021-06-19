#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverse(n,r):
    if n==0:
        return r
    
    else:
        return reverse(n//10, (r * 10 + n % 10))
    
n = int(input())
reverse(n,0)

