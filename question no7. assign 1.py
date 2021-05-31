#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd


# In[11]:


import numpy as np


# In[12]:


import matplotlib as mpl


# In[13]:


import seaborn as sns


# In[16]:


df = pd.read_csv("E:\Data Science\Q7.csv")


# In[17]:


df.head(33)


# In[18]:


df['Points'].mode()


# In[21]:


df['Score'].mode()


# In[22]:


df['Weigh'].mode()


# In[23]:


df.mean()


# In[24]:


df.var()


# In[25]:


df.std()


# In[26]:


df.median()

