#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def merge(l):
    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i = i+1
                k = k+1

            else:
                l[k] = right[j]
                j = j+1
                k = k+1

        while i < len(left):
            l[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            l[k] = right[j]
            j = j+1
            k = k+1
            
l = [6,9,7,3,0,1]
merge(l)
print(l)

