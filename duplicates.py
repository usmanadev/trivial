#!/usr/bin/env python
# coding: utf-8

# In[11]:


def duplicates(items):
    """Returns a list of identified duplicate elements.
    """
    dups = set()
    for i in items:
        if items.count(i) > 1:
            dups.add(i)
    return list(dups)

