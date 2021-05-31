#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as mpl
import seaborn as sns
import numpy as np


# In[2]:


Cars_df=pd.read_csv("Cars.csv")


# In[3]:


Cars_df


# In[11]:


if Cars_df['MPG'].mean() == Cars_df['MPG'].median() == stats.mode(cars['MPG']):
    print('MPG follows normal distribution')
else:
    print('MPG does not follow normal distribution')


# In[ ]:





# In[ ]:




