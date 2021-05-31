#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib as mpl


# In[4]:


import seaborn as sns


# In[11]:


q9_a_df = pd.read_csv("Q9_a.csv")


# In[12]:


q9_a_df


# In[13]:


q9_a_df.skew()


# In[14]:


q9_a_df.kurt()


# In[15]:


q9_a_df.columns


# In[17]:


pd.crosstab(q9_a_df.speed,q9_a_df.dist)


# In[21]:


pd.crosstab(q9_a_df.speed,q9_a_df.dist).plot(kind='bar')


# In[ ]:




