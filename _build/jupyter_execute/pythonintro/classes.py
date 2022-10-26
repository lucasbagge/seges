#!/usr/bin/env python
# coding: utf-8

# # Object-Oriented Programming
# 
# Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
# 
# For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.
# 
# Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.
# 
# ## How to Define a Class
# 
# All class definitions start with the class keyword, which is followed by the name of the class and a colon. Any code that is indented below the class definition is considered part of the class’s body.
# 
# Here’s an example of a Dog class:
# 
# ```python
# class Dog:
#     pass
# ```
# 
# The properties that all Dog objects must have are defined in a method called `.__init__()`. Every time a new Dog object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.
# 
# You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When a new class instance is created, the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.
# 
# Let’s update the Dog class with an .__init__() method that creates .name and .age attributes:

# In[1]:


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In the body of .__init__(), there are two statements using the self variable:
# 
# 1) self.name = name creates an attribute called name and assigns to it the value of the name parameter.
# 2) self.age = age creates an attribute called age and assigns to it the value of the age parameter.
# 
# Attributes created in .__init__() are called **instance attributes**. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.
# 
# On the other hand, **class attributes** are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
# 
# For example, the following Dog class has a class attribute called species with the value "Canis familiaris":
# 
# ```python
# class Dog:
#     # Class attribute
#     species = "Canis familiaris"
# 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```
# 
# Class attributes are defined directly beneath the first line of the class name and are indented by four spaces. They must always be assigned an initial value. When an instance of the class is created, class attributes are automatically created and assigned to their initial values.
# 
# Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.
# 
# ## Exercies
# 
# ### Exercise 11.1 (PersonReader)
# 
# Implement a class PersonReader supporting the following methods:
# 
# input() asks the user for the name and year of birth of a person at shell prompt (using the builtin input function).
# 
# __str__ that returns the string 'name (year)' (e.g. to be used by the print method when applied to a PersonReader).
# 
# Example.
# 
#  M = PersonReader()
#  M.input()
# Name: Margrethe
# Born: 1940
#  print(M)
# Margrethe (1940)

# In[2]:


class PersonReader:
    def __init__(self):
        self.name = None
        self.year = None
    
    def input(self):
        self.name = input('name: ',)
        self.year = input('year: ')
    
    def __str__(self):
        return f'{self.name} ({self.year})'


# In[3]:


M = PersonReader()
M.input()


# 

# In[10]:


print(M)


# ### Exercise 11.3 (2D vector)
# 
# In this exercise you should implement a class Vector for storing 2D vectors with the two vector coordinates as the attributes x and y. The class should have the following methods:
# 
# * A constructor __init__ where it is possible to create a new vector using Vector(x, y).
# 
# * length() returning the length of the vector, i.e. sqrt(x ** 2 + y ** 2). Hint. from math import sqrt.
# 
# * add(other_vector) return a new vector that is the result of adding two vectors.
# 
# * Redefine + so that vector1 + vector2 returns a new vector that is the sum of the two vectors (i.e. define __add__).
# 
# * mult(factor), where factor is an int or float, should return a new vector Vector(x * factor, y * factor).
# 
# * dot(vector) should return the dot product with another vector, i.e. x * vector.x + y * vector.y.
# 
# * Define the * operator so that vector * number returns vector.mul(number) whereas vector1 * vector2 returns the dot product of the two vectors (i.e. define __mul__).
# 
# * Define __rmul__ so that it possible to write number * vector. The result should be the same as vector * number.
# 
# * Define __str__ to return the string '<x, y>' where x and y are the coordinates of the vector.

# In[29]:


from math import sqrt
import numpy as np

class Vector():
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.vector = [x, y]
        
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def add(self, other_vector):
            return [(self.x + other_vector, other_vector + self.y)]


# In[30]:


t = Vector(x = [1, 1], y = [2,1])

t.length()


# In[31]:


t.add([1,1])


# ## FRAGILE VALUES
# 
# In this problem you should implement a class FragileValue, where
# each FragileValue object stores a nonnegative integer, e.g.
# FragileValue(42) should create an object storing the value 42.
# The class FragileValue should support the addition of two FragileValue
# objects, i.e. the + operator between two FragileValue objects, and
# printing a FragileValue, i.e. supporting str(x) where x is a
# FragileValue object.
#     
# Whenever str(x) is called on a FragileValue x, the value stored in the
# FragileValue is decreased by one before the value is returned as a
# string. Similarly, x + y should decrease the values of both x
# and y by one, before returning a FragileValue containing the sum of the
# new values of x and y. Note that print(FragileValue(5) + FragileValue(7))
# prints 9, since the addition first decreases the two FragileValues to
# 4 and 6, respectively, before creating a new FragileValue storing 10.
# Printing this FragileValue first decreases its value to 9, before
# printing the string '9'.
#     
# If a FragileValue stores the value zero before calling str on it, or
# before adding it with another FagileValue value, a BrokenValue exception
# should be raised.
# 
#     Input:  Multiple lines of Python code using the class FragileValue.
#             The last line should start with '#eof' (indicating end of file).
# 
#     Output: The output generated by executing the input code.
#             If the code throws a BrokenValue exception,
#             'BrokenValue' should be printed and the program end normally.
# 
#     Example:
# 
#       Input:  x = FragileValue(42)
#               print(x)
#               print(x)
#               x = FragileValue(5)
#               y = FragileValue(7)
#               z = x + y
#               print(z)
#               #eof
# 
#       Output: 41
#               40
#               9
# 
#     Note: The below code already handles reading input, executing the input,
#           and handling a raised BrokenValue exception.
# 

# In[ ]:


class BrokenValue(Exception):
    pass

