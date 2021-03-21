#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mean(items):
    return sum(items) / len(items)

def median(items):
    n = len(items)
    mid = n // 2
    if n % 2:
        return sorted(items)[mid]
    else:
        return sum(sorted(items))[mid - 1:mid + 1] / 2
    
def mode(items):
    return max(items, key = items.count)


# In[ ]:




