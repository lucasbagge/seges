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


# In[2]:


k, k1, k2, k3 = [3, 2, 5], [2, 7, 9], [1, 2], [1,21,1]


def my_map_k(a, *b):
    return [a(*l) for l in zip(*b)]

f = lambda x, y : x * y

[f(x, y) for x, y in zip(k, k1)]


# In[3]:


my_map_k(lambda x, y, z: x * y * z, [3, 2, 5], [2, 7, 9], [1, 2])


# ### Exercise 10.2 (string sorting)
# 
# Write a function str_sort that sorts a list of strings, such that the strings are sorted with respect to the number of distinct letters ('a' - 'z') there are in the strings. Strings with an equal number of distinct letters after converting to lower case should apper in alphabetical order.
# 
# Example.
# 
# str_sort(['AHA', 'Oasis', 'ABBA', 'Beatles', 'AC/DC', 'B. B. King', 'Bangles', 'Alan Parsons'])
# should return
# 
# ['ABBA', 'AHA', 'AC/DC', 'Oasis', 'B. B. King', 'Beatles', 'Alan Parsons', 'Bangles']`.
# Hint. Use len(set(X)) to find the number of different elements in a list X.

# In[4]:


t = 'ABBA'

len(set(t))


# In[5]:


tt = 'B. B. King'
len(set(tt))


# In[6]:


[c for c in tt.lower() if c.isalpha() ]


# In[7]:


def str_sort(L):
    return sorted(L, key= lambda x: (len(set([c for c in x.lower() if c.isalpha()])), x))


# In[8]:


str_sort(['AHA', 'Oasis', 'ABBA', 'Beatles', 'AC/DC', 'B. B. King', 'Bangles', 'Alan Parsons'])


# ### Exercise 10.4* (foldr)
# 
# In this exercise the goal is to make an implementation of foldr (fold right). Python's reduce function is often called foldl (fold left) in other programming languages, that given a function f and a list [x1, x2, x3, ..., xn] computes f(f(···f(f(x1, x2), x3)···), xn).
# 
# The function foldr should instead compute f(x1, f(x2, f(x3, f(···f(xn-1, xn)···)))).
# 
# This function does not appear in the Python standard library but is standard in other programming languages, in particular functional programming languages like Haskell and ML. The difference between folding left and right is illustrated by applying the power function to the list [2, 2, 2, 2], where ((2 ** 2) ** 2) ** 2 == 256 whereas 2 ** (2 ** (2 ** 2)) == 65536.
# 
# import functools
# foldl = functools.reduce
# 
# def foldr(f, L):
#     # your code
# 
# print(foldl(lambda x, y: x ** y, [2, 2, 2, 2]))     # prints 256
# print(foldr(lambda x, y: x ** y, [2, 2, 2, 2]))     # should print 65536
# print(foldr(lambda x, y: x ** y, [2, 2, 2, 2, 2]))  # value with 19729 digits
# Note. You can implement foldr both with a loop and recursively.

# In[9]:


t = [2, 2, 2, 2]
[x**2 for x in t]


# In[10]:


from functools import reduce
def foldr(op, lst):
    return reduce(op, reversed(lst))

foldr(lambda x, y: x ** y, [2, 2, 2, 2])


# In[11]:


print(foldr(lambda x, y: x ** y, [2, 2, 2, 2, 2]))


# In[ ]:




