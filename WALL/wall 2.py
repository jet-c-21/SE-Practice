#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind


# In[2]:


import weakref


# In[3]:


stock = weakref.WeakValueDictionary()


# In[4]:


catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]


# In[6]:


for cheese in catalog:
    stock[cheese.kind] = cheese


# In[8]:


print(sorted(stock.keys()))


# In[9]:


del catalog


# In[10]:


print(sorted(stock.keys()))


# In[11]:


del cheese


# In[12]:


print(sorted(stock.keys()))


# In[ ]:



