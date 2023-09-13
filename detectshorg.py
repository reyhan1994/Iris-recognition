#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import os
import glob
import time


# In[2]:


face_cascade = cv2.CascadeClassifier('J:\\INanaconda\\haarcascade_frontalface_default.xml');
eye_cascade = cv2.CascadeClassifier('I:/Input_output/cascade/haarcascade_mcs_righteye.xml');


# In[3]:


import os
data_dir = 'C:\\Users\\Sepehr Rayaneh\\Desktop\\diss'
print(data_dir)
for item in os.listdir(data_dir):
    path=os.path.join(data_dir,item)
    print(path)
    counter=0
    for img in os.listdir(path):
        counter += 1
        pathwrite=os.path.join(path,str(counter)+'.jpg')
        pathimage=os.path.join(path,img)
        print(pathimage)
        img=cv2.imread(pathimage)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        eyes = eye_cascade.detectMultiScale(gray,4.90, 13)
        for (x,y,w,h) in eyes:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv2.imwrite(pathwrite,roi_gray)
            
        


# In[ ]:




