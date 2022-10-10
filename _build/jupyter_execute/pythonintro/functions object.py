#!/usr/bin/env python
# coding: utf-8

# # Functions objects

# ## Exercise 10.1 (my_map)
# 
# In this exercise the goal is make your own implementation of Python's builtin map function.
# 
# 1) Make a function my_map that takes two arguments, a function f and a list [x1, ..., xn], and returns the list [f(x1), ..., f(xn)].
# 
# Example. my_map(lambda x: x ** 3, [3, 2, 4])) should return [27, 8, 64].
# 
# 2) Make a function my_map_k that as arguments takes a function f requiring k ≥ 1 arguments and k lists L1, ..., Lk, and returns the list [f(L1[0], ..., Lk[0]), ..., f(L1[n-1], ..., Lk[n-1])], where n is the length of the shortest Li list.
# 
# Hint. Use Python's * notation to handle an arbitrary number of lists as arguments.
# 
# Example. my_map_k(lambda x, y, z: x * y * z, [3, 2, 5], [2, 7, 9], [1, 2]) should return [6, 28].
# 
# Note. Your solution should not use the builtin map function.

# In[1]:


def my_map(a, b):
    return [a(l) for l in b]

my_map(lambda x: x ** 3, [3, 2, 4])


# In[ ]:




