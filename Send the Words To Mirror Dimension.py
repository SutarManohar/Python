#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reverse(s):
    str = " "
    for i in s:
        str = i + str
    return str

print("Enter the input word")
word = input()

print("The original input string is :",end = " ")
print(word)

print("The reverse string is :",end = " ")
print(reverse(word))

