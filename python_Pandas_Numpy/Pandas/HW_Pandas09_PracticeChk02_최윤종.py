
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[12]:


s = pd.Series(['1.Ant. ','2. Bee!\n', '3. Cat?\t', np.nan])
s


# In[14]:


s.str.strip()


# In[15]:


s.str.strip(',')


# In[16]:


s.str.strip('123.!?\n\t')


# In[17]:


s.str.lstrip('123.')


# In[18]:


s.str.rstrip('.!?\n\t')


# In[19]:


s.str.strip('123.!? \n\t')

