#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def water(a):
    area = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            area = max(area, min(a[i], a[j]) * (j - 1))
    return area
a = [3, 1, 2, 4, 5]
water(a)

