#!/usr/bin/env python
# coding: utf-8

# In[5]:


my_str = 'The quick Brow Fox'

def case(my_str):
    upper=0
    lower=0
    for i in my_str:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1

    print("No. of Upper case characters :", upper)
    print("No. of Lower case characters :", lower)

case(my_str)

