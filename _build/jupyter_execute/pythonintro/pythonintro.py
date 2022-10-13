#!/usr/bin/env python
# coding: utf-8

# # Python functions

# In python you can easy define a function using the syntacs:
# 
# ```python
# def functino-name(var_1,...var_k):
#     return body code
# ```
# 
# Where as in R we give the functoin some variables/parameter and it return s ouput. 
# 
# Let us see an example:
# 

# In[1]:


def sum3(x, y, z):
    return x+y+z

print('test function \n', sum3(2,2,2))


# ## Multiple arguments
# 
# If you dont want to specifie every variable that goes into your function you can add `*variable`:

# In[2]:


def my_print(x, y, *L):
    print('x = ', x)
    print('y = ', y)
    print('L = ', L)
    
my_print(1, 2, 3, 4, 5, 56,3,2 ,1)    


# ## Arbitrary Keyword Arguments, **kwargs
# 
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# 
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# In[3]:


def my_func(**L):
    print('his name is ' + L['fname'])
    
my_func(fname = 'Lucas')


# ## Exercises
# 
# ### Exercise 7.1 (average)
# 
# 

# #### Write a function average_two(x, y) that computes the average of x and y, i.e. (x + y )/2.
# 
# 

# In[4]:


def average_two(x, y):
    return (x + y) / 2

print(average_two(2, 1))


# #### Write a function list_average(L) that computes the average of the numbers in the list L.
# 
# 

# In[5]:


def list_a(L):
    return sum(L) / len(L)

Lt = [1, 2, 1, 5]

print(list_a(Lt))


# #### Write a function average(x1, ..., xk) that takes an arbitrary number of arguments (but at least one) and computes the average of x1, ..., xk.
# 
# Hint. Use a * to indicate an arbitrary argument list.

# In[6]:


def avv(*x):
    return list_a(list(x))

Lt = 1
l2 =  2

print(avv(Lt, l2, 1, 1))


# In[ ]:




