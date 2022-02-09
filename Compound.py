#!/usr/bin/env python
# coding: utf-8

# In[1]:


class comp_int:
    def __init__(self):
        self.p=0.0
        self.r=0.0
        self.t=0.0
    
        
        
    def CI(self):
        self.p=float(input('enter principle amount= '))
        self.r=float(input('enter rate of interest= '))
        self.t=float(input('enter time= '))
        a=self.p*(1+0.01*self.r)**self.t
        return a


# In[ ]:




