#!/usr/bin/env python
# coding: utf-8

# In[8]:


def consonant_words(string):
    """Returns a list of words that have consonants only.
    """
    vowel = 'aeiouAEIOU'
    word_list = string.split()
    cons_list = []
    for word in word_list:
        for letter in word:    
            if letter in vowel:
                break
        else:
            cons_list.append(word)
    return cons_list

