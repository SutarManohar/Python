#!/usr/bin/env python
# coding: utf-8

# In[1]:


# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers: [3, 6, 9, 12, 15, 18, 21]

sample_list = [1, 2, 3, 4, 5, 6, 7]
print("sample_list: ", sample_list)
result = map(lambda x: x + x + x, sample_list) 
print("\nTriple of list numbers:", list(result))

