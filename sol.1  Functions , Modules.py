#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers = (8, 2, 3, 0, 7)
   
def add(numbers):
    count=0
    for i in range(len(numbers)):
        count+=numbers[i]
    return count
add(numbers)

