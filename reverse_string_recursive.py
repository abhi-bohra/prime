#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverse(s):
        if len(s) == 0:
            return s
        else:
            return reverse(s[1:]) + s[0]
    
s = input('Enter a string:')
reverse(s)


# In[ ]:




