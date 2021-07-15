#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find3Numbers():
    n = len(nums)
    count = 0
    nums.sort()
 
    for i in range(0, n-1):
        l = i + 1
        r = n-1
        while (l < r):
            if( nums[i] + nums[l] + nums[r] == 0):
                print(nums[i], nums[l], nums[r])
                l += 1
                r -= 1
                count = count + 1
                
            elif (nums[i] + nums[l] + nums[r] < 0):
                l += 1
            else:
                r -= 1
    
    if count == 0:
        return ('No triplets found')

nums = [0, -1, 2, -3, 1]
 
find3Numbers()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




