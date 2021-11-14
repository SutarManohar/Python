#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict = {}
 
# Now populate it
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dict[chr(i)] = i
 
print(my_dict)

