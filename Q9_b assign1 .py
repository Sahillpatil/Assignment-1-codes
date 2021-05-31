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


# In[7]:


q9_b_df = pd.read_csv("Q9_b.csv")


# In[8]:


q9_b_df


# In[10]:


q9_b_df.skew()


# In[12]:


q9_b_df.kurt()


# In[13]:


q9_b_df.columns


# In[15]:


pd.crosstab(q9_b_df.SP,q9_b_df.WT)


# In[17]:


pd.crosstab(q9_b_df.SP,q9_b_df.WT).plot(kind='bar')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




