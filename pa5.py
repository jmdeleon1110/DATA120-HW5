#!/usr/bin/env python
# coding: utf-8

# 0.0.1 Problem 1: GCD

# In[1]:


def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        return gcd(a, b % a)
    if b < a:
        return gcd(b, a % b)


# 0.0.2 Problem 2: Directions

# In[40]:


def remove_pairs(directions):
    turnarounds = {'EW', 'WE', 'NS', 'SN'}

    if len(directions) <= 1:
        return directions
    
    pair = directions[:2]
    if pair in turnarounds:
        return remove_pairs(directions[2:])
    else:
        return directions[0] + remove_pairs(directions[1:])


# In[39]:


remove_pairs('EEWN')


# In[41]:


remove_pairs('SSNS')


# In[42]:


remove_pairs("ESNW")


# 0.0.3 Problem 3: Bisection Method

# In[56]:


def bisection_root(equation, x1, x2):
    
    if equation(x1)<0 and equation(x2)<0 or equation(x1)>0 and equation(x2)>0:
        raise ValueError('Cannot find the root between these values')
        
    if abs(equation(x1))<.001:
        return x1
    
    if abs(equation(x2))<.001:
        return x2
    
    else: 
        x = (x1 + x2) / 2
        y = equation(x)
        
        if (x >= 0) != (x1 >= 0):
            bisection_root(equation, x, x1)
        if (x >= 0) != (x2 >= 0):
            bisection_root(equation, x, x2)
    return x


# In[54]:


import math


# In[55]:


bisection_root(math.sin,2, 4)


# In[ ]:




