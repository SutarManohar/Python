#!/usr/bin/env python
# coding: utf-8

# In[10]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 1:
        even = even+1
    else:
        odd = odd+1

print("Number of even numbers :",even)
print("Number of odd numbers :",odd)

