#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib as mpl
import seaborn as sns
import numpy as np


# In[6]:


Cars_df=pd.read_csv("Cars.csv")


# In[7]:


Cars_df


# In[9]:


Cars_df=Cars_df[['MPG']]


# In[10]:


Cars_df


# In[11]:


Cars_df.mean()


# In[12]:


Cars_df.std()


# In[13]:


from scipy import stats


# In[14]:


stats.norm.cdf(38,loc=34.422076,scale=9.131445)


# In[15]:


1-stats.norm.cdf(38,loc=34.422076,scale=9.131445)


# In[16]:


stats.norm.cdf(40,loc=34.422076,scale=9.131445)


# In[17]:


data1=stats.norm.cdf(50,loc=34.422076,scale=9.131445)


# In[18]:


data1


# In[19]:


data2=1-stats.norm.cdf(20,loc=34.422076,scale=9.131445)


# In[20]:


data2


# In[21]:


data2-data1

