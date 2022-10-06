#!/usr/bin/env python
# coding: utf-8

# # Python Recursion
# 
# 

# The idea behind recursion is simple;
# > Write a functoin that repeat itself.
# 
# Let us look at at example where we iterate though a loop that prints its number until it each zero:

# 

# In[1]:


def countdown(n):
    if n <= 0:
        print('blastoff')
    else:
        print(n)
        countdown(n - 1)
countdown(3)        


# For applying recursion you need to orby three laws:
# 
# 1) A recursive algorithm must have a base case.
# 2) A recursive algorithm must change its state and move toward the base case.
# 3) A recursive algorithm must call itself, recursively.
# 
# Let’s look at each one of these laws in more detail. First, a base case is the condition that allows the algorithm to stop recursing. A base case is typically a problem that is small enough to solve directly. In the countdown algorithm the base case is when the number is 0.
# 
# To obey the second law, we must arrange for a change of state that moves the algorithm toward the base case. A change of state means that some data that the algorithm is using is modified. Usually the data that represents our problem gets smaller in some way.
# 
# The final law is that the algorithm must call itself. This is the very definition of recursion. Recursion is a confusing concept to many beginning programmers. As a novice programmer, you have learned that functions are good because you can take a large problem and break it up into smaller problems. The smaller problems can be solved by writing a function to solve each problem. When we talk about recursion it may seem that we are talking ourselves in circles. We have a problem to solve with a function, but that function solves the problem by calling itself! But the logic is not circular at all; the logic of recursion is an elegant expression of solving a problem by breaking it down into a smaller and easier problems.
# 
# Another way of explaining it is for the Russian **Matryoshka DoLL** that hase multiple dolls inside of it. 

# ## Exercises
# 
# ### Exercise 8.1 (upper and lower cases)
# 
# Make a recursive function cases(s) that given a string s, generates a list of all possible upper and lower case combinations of the letters in the string. E.g. cases('abcB') should return a list containing the following 16 strings ['abCb', 'abCB', 'abcb', 'abcB', 'aBCb', 'aBCB', 'aBcb', 'aBcB', 'AbCb', 'AbCB', 'Abcb', 'AbcB', 'ABCb', 'ABCB', 'ABcb', 'ABcB'].

# In[2]:


def cases(s):
    if s == "":  # Base Case
        return [""]

    hoved = s[0]
    haler = cases(s[1:])
    Case = [hoved.lower(), hoved.upper()]  #)
    return [case + hale for case in Case for hale in haler]


# In[3]:


s = 'abcB'

cases(s)


# ### Exercise 8.2 (list subsets)
# 
# Make a recursive function subsets(L) that given a list L returns a list of all subsets of L (each subset being a list). E.g. subsets([1, 2]) should return [[], [1], [2], [1, 2]]. The order of the returned lists can be arbitrary.

# In[4]:


def l_s(ls):
    if ls == []:
        return [[]]
    
    x = l_s(ls[1:])
    
    return x + [[ls[0]] + y for y in x]


# In[5]:


lls = [1, 2]
l_s(lls)


# ### Exercise 8.3 (tree relabeling)
# 
# Make a recursive function relabel(tree, new_names) that takes a tree tree and a dictionary new_names = {old_name: new_name, ...}, and returns a new tree where labels in the dictionary new_names are replaced by the corresponding values in the dictionary. Leaves not in the dictionary remain unchanged.
# 
# Example. relabel(('a', ('b', 'c')), {'a': 'x', 'c': 'y'}) should return ('x', ('b', 'y')).
# 
# 

# In[6]:


def relabel(tree, new_names):
    if isinstance(tree, str):
        return new_names.get(tree, tree)
    else:
        return tuple([relabel(child, new_names) for child in tree])


# In[7]:


relabel(('a', ('b', 'c')), {'a': 'x', 'c': 'y'})


# ### Exercise 8.4 (validate leaf-labeled binary trees)
# 
# Assume we want to represent binary trees, where each leaf has a string as a label, by nested tuples. We require the leaves are labeled with distinct non-empty strings and all non-leaf nodes have exactly two children. E.g. ((('A', 'B'), 'C'), ('D', ('F', 'E'))) is a valid binary tree.
# 
# Write a function validate_string_tuple(t) that checks, i.e. returns True or False, if the value t is a tuple only containing distinct strings, e.g. ('a', 'b', 'c').
# 
# Write a recursive function valid_binary_tree(tree) program that checks, i.e. returns True or False, if the value tree is a recursive tuple representing a binary tree as described above.
# 
# Hint. Use the method isinstance to check if a value is of class tuple or a str, and use a recursive function to traverse a tree. Collect all leaf labels in a list, and check if all leaves are distinct by converting to set.

# In[8]:


def validate_string_tuple(t):  # fancy
    return isinstance(t, tuple) and all(
        [isinstance(c, str) for c in t]) and len(t) == len(set(t))
tt = ((('A', 'B'), 'C'), ('D', ('F', 'E')))
validate_string_tuple(tt)


# ### Exercise 8.6 - handin 4 (triplet distance - part II)
# 
# This handin is a continuation of the previous handin. The code from the previous handin should be reused in this exercise. In this second part the aim should be to write elegant recursive code using Python's tuples and list comprehensions.
# 
# Make a recursive function generate_tree(labels), that given a list of labels labels, returns a random binary tree where the list of leaf labels from left to right in the tree equals labels.
# 
# Hint. Split the list labels at a random position into two nonempty parts left and right, and recursively construct the trees for the two parts.
# 
# Example. generate_tree(['A', 'B', 'C', 'D', 'E', 'F']) could return ((('A', ('B', 'C')), ('D', 'E')), 'F')
# 
# Make a recursive function generate_triplets(tree) that returns a pair (labels, triplets) where labels is a list of all leaf labels of tree, and triplets is a list of all canonical triplets anchored at some node of tree.
# 
# Hint. Use isinstance(tree, str) to check if tree is a leaf.
# 
# Example. generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E')))) should return the following pair consisting of a list with the 6 leaf labels, and a list with the 20 canonical triplets anchored in the tree: (['A', 'F', 'B', 'D', 'C', 'E'], [('B', ('A', 'F')), ('D', ('C', 'E')), ('A', ('D', 'E')), ('A', ('C', 'D')), ('A', ('C', 'E')), ('F', ('D', 'E')), ('F', ('C', 'D')), ('F', ('C', 'E')), ('B', ('D', 'E')), ('B', ('C', 'D')), ('B', ('C', 'E')), ('D', ('A', 'F')), ('D', ('A', 'B')), ('D', ('B', 'F')), ('C', ('A', 'F')), ('C', ('A', 'B')), ('C', ('B', 'F')), ('E', ('A', 'F')), ('E', ('A', 'B')), ('E', ('B', 'F'))])
# 
# Make a function triplet_distance(tree1, tree2) that computes the triplet distance between the trees tree1 and tree2.
# 
# Hint. Recall that the triplet distance equals n · (n - 1) · (n - 2) / 6 minus the number of common triplets between tree1 and tree2, where n is the number of common labels in tree1 and tree2, and use Python set to handle the sets of computed triplets.
# 
# Example. For the two trees above
# 
# triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))), (((('D', 'A'), 'B'), 'F'), ('C', 'E'))
# should return 10.
# 
# What is the order of the tree sizes you can handle with generate_tree and triplet_distance in reasonable time - say about 10 seconds? Tens, hundreds, thousands, millions... of leaves? Use the function generate_tree to generate random trees of increasing sizes and measure the time for generate_tree and triplet_distance separately.
# 
# (Optional) Make a function print_ascii_tree(tree) to print trees like the ones shown in part I of this exercise.

# In[9]:


from random import randint
from time import time


# In[10]:


def generate_tree(L):
    # base case
    if len(L) == 1: 
        return L[0]
    split = randint(1, len(L)-1)
    left = L[:split]
    right = L[split:]
    return (generate_tree(left), generate_tree(right))

L = ['A', 'B', 'C', 'D', 'E', 'F']
print("a) Træer: " ,generate_tree(L))


# In[11]:


# b)

# canonical_triplets er fra sidste afleverin
def canonical_triplets(A, B):
  can = [(x, (y,z)) for x in A for y in B for z in B if y < z]
  return can

# anchored_triplets er fra sidste afleverin
def anchored_triplets(A,B):
  left = canonical_triplets(A,B)
  right = left
  right += canonical_triplets(B,A)
  return list(( right))

def generate_triplets(T):
  if isinstance(T, str):
    return [T], []
  else:
    left = T[0]
    right = T[1]
    
    left_labels, left_triplets = generate_triplets(left)
    right_labels, right_triplets = generate_triplets(right)
    
    labels = left_labels + right_labels
    triplets = left_triplets + right_triplets
    
    anchored_triplet = anchored_triplets(left_labels, right_labels)
  return labels, triplets + anchored_triplet

print("b) output: " ,generate_triplets(((('A','F'),'B'),('D',('C','E')))) )


# In[12]:


def triplet_distance(T1, T2):
  gen_T1 = generate_triplets(T1)
  gen_T2 = generate_triplets(T2)
  
  n = len(gen_T1[0])
  x = gen_T1[1]
  y = gen_T2[1]
  
  intersec = len(set(x) & set(y))
  
  return (n * (n - 1) * (n - 2)) // 6 - intersec

print("c) distance between trees: ",triplet_distance(((('A','F'),'B'),('D',('C','E'))), (((('D','A'),'B'),'F'),('C','E'))) )


# In[ ]:




