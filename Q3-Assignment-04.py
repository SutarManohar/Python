#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sample List: [4, 5, 2, 9]
# Square the elements of the list: [16, 25, 4, 81]

Sample_List = [4, 5, 2, 9]
def square_Sample_List(n):
  return n * n

print("Original List: ",Sample_List)
result = map(square_Sample_List, Sample_List)
print("Square the elements of the list:", list(result))

