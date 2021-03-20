#!/usr/bin/env python
# coding: utf-8

# In[16]:


def reverse_string_by_words(string):
    """Reverses a string word by word.
    """
    split_str = string.split()
    rev_str = []
    for i in reversed(split_str):
        rev_str.append(i)
    rev_str = ' '.join(rev_str)
    return rev_str

