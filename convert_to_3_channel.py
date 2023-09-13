#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf


# In[ ]:


tf.enable_eager_execution()
tf.__version__


# In[ ]:


import pathlib
import random
import os


# In[ ]:


from google.colab import drive
 
# This will prompt for authorization.
drive.mount('/mydrive')


# In[ ]:


# Load the Drive helper and mount
from google.colab import drive
 
# This will prompt for authorization.
drive.mount('/mygoogledrive')
 
get_ipython().system('ls /mygoogledrive')
 
get_ipython().system("ls '/mygoogledrive/My Drive'")
 
 
import os
 
mydrive_path = '/mygoogledrive/My Drive'
mydrive = os.listdir(mydrive_path)
 
for f in mydrive: 
  print(f)


# In[ ]:


from google.colab import files
os.chdir('/mygoogledrive/My Drive/')
os.getcwd()


# In[ ]:


train_dir='/mygoogledrive/My Drive/sunday/train/'


# In[ ]:


data_root=f'{train_dir}'
data_root = pathlib.Path(data_root)
all_image_paths = list(data_root.glob('*/*'))
all_image_paths = [str(path) for path in all_image_paths]


# In[ ]:


img_path = all_image_paths[0]
img_path


# In[ ]:


img_raw = tf.io.read_file(img_path)
print(repr(img_raw)[:100]+"...")


# In[ ]:


img_raw = tf.io.read_file(img_path)


# In[ ]:


img_tensor = tf.image.decode_image(img_raw)

print(img_tensor.shape)
print(img_tensor.dtype)


# In[ ]:


image = tf.image.grayscale_to_rgb(img_tensor)


# In[ ]:


print(image.shape)
print(image.dtype)


# In[ ]:




