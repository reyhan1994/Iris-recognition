#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import sys
import random
import numpy as np
import glob
#from glob import glob
import shutil
from tqdm import tqdm
import pathlib


# In[6]:


DATA_DIR =  'I:\\New folder'
train_dir = 'I:\\New folder'
valid_dir = 'I:\\all'


# In[7]:


#os.listdir(train_dir)


# In[8]:


print(train_dir)
files=os.listdir(train_dir)
print(files)
for f in files:
    base=os.path.basename(f)
    a=os.path.splitext(base)
    if '.bmp' in f:
        shutil.move(train_dir + '/'+a[0]+'.bmp',valid_dir+'/'+a[0]+'.bmp')


# In[12]:



data_dir= 'I:\\New folder'
for item in os.listdir(data_dir):
    #print(item)
    path=os.path.join(data_dir,item)
    print(path)
    files=os.listdir(path)
    print(files)
    for f in files:
        base=os.path.basename(f)
        a=os.path.splitext(base)
        if '.bmp' in f:
            shutil.move(path+ '/'+a[0]+'.bmp',valid_dir+'/'+a[f+1]+'.bmp')


# In[ ]:




