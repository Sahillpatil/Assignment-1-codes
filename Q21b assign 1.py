#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns


# In[3]:


wc_at=pd.read_csv("wc-at.csv")


# In[4]:


wc_at


# In[5]:


if wc_at['AT'].mean() == wc_at['AT'].median() == stats.mode(wc_at['AT']):
    print('AT follows normal distribution')
else:
    print('AT does not follow normal distribution')
    
if wc_at['Waist'].mean() == wc_at['Waist'].median == stats.mode(wc_at['Waist']):
    print('\n Waist follows normal distribution')
else:
    print('\n Waist does not follow normal distribution')
        

