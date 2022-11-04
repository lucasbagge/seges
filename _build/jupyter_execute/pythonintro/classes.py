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

# In[1]:


class BrokenValue(Exception):
    pass

class FragileValue():
    def __init__(self, value):
        assert value >= 0
        self.value = value
        
    def __add__(self, other):
        if self.value ==  0 or other.value == 0:
            raise BrokenValue
        self.value -= 1
        other.value -= 1
        return FragileValue(self.value + other.value)
    
    def __str__(self):
        if self.value == 0:
            raise BrokenValue
        self.value -= 1
        return str(self.value)
        


# In[4]:


x = FragileValue(42)


# In[5]:


print(x)


# In[ ]:


x = FragileValue(5)
y = FragileValue(7)


#     ROTATING VECTOR
# 
#     Your task is to create a class Vector to represent two-dimensional vectors.
#     An object v of class Vector should be created by v = Vector(x, y),
#     where x and y are floats. Create methods mult and rotate: 
#     v.mult(c) should scale the x and y coordinates by the float c, and
#     v.rotate() should rotate the vector 90 degrees counter clockwise.
#     Both mult and rotate should change the vector and return None.
#     Finally, define __str__ (used by str and print) to return the string
#     'Vector(x, y)', where the x and y coordinates are shown with 3 decimals.
# 
#     Example of usage:
#     
#         > v = Vector(1.0, 3.0)
#         > print(v)
#         Vector(1.000, 3.000)
#         > v.rotate()
#         > print(v)
#         Vector(-3.000, 1.000)
#         > v.mult(0.5)
#         > print(v)
#         Vector(-1.500, 0.500)
# 
#     Input:  A Python expression using the class Vector.
# 
#     Output: The output generated by evaluating the input expression.
# 
#     Example:
# 
#       Input:  print(*[x for v in [Vector(2.0, 1.0)] for x in [str(v), v.rotate(), v.mult(1 / 3), str(v)]])
#     
#       Output: Vector(2.000, 1.000) None None Vector(-0.333, 0.667)
#  
#     Note: The below code already takes care of handling the input and output.

# In[26]:


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar
    
    def rotate(self):
        self.x, self.y = -self.y, self.x
        
    def __str__(self):
        return f'Vector({self.x}, {self.y})'
        
    


# In[27]:


v = Vector(1.0, 3.0)
#v.mult(0.5)
v.rotate()
print(v)


# GENEALOGY
# 
#     Your task is to create a class Student to represent a student
#     with a name and advisor information. Student(name) should create
#     a new Student object with the given name (a string), whereas
#     Student(name, advisor) creates a student with an associated
#     advisor (a Student object).
#     The Student class should have two additional methods ancestors()
#     and descendants(). The ancestors method should return a list with
#     the advisor's name and recursive the advisor's ancestors names.
#     The list of names should be alphabetically sorted.
#     The descendants method should return a list with the names of the
#     students an advisor has had, and recursively their descendants.
#     The list of names should be alphabetically sorted.
# 
#     Example of usage:
#     
#         Ancestor tre:
#     
#                  Peter
#                  /   \
#                 /     \
#               Tom    Simon
#                |
#                |
#               Dora  
# 
#         > peter = Student('Peter')
#         > tom = Student('Tom', advisor=peter)
#         > simon = Student('Simon', advisor=peter)
#         > dora = Student('Dora', advisor=tom)
#         > print(dora.ancestors())
#         ['Peter', 'Tom']
#         > print(peter.descendants())
#         ['Dora', 'Simon', 'Tom']
# 
#     Input:  A single line with Python statements separated by semicolon.
# 
#     Output: The output generated by evaluating the input line.
# 
#     Example:
# 
#       Input:  peter = Student('Peter'); tom = Student('Tom', advisor=peter);
#               simon = Student('Simon', advisor=peter); dora = Student('Dora',
#               advisor=tom); print(dora.ancestors()); print(peter.descendants())
# 
#               (a single line with the above usage example)
#               
#       Output: ['Peter', 'Tom']
#               ['Dora', 'Simon', 'Tom']
#  
#     Note: The below code already takes care of handling the input and output.

# In[8]:


class Student:
    def __init__(self, name, advisor = None):        
        self.name = name
        self.advisor = advisor
        self.students = []
        if advisor:
            advisor.students.append(self)
            
    def ancestors(self):
        if not self.advisor:
            return []
        return sorted([self.advisor.name] + self.advisor.ancestors())
    
    def descendants(self):
        names = []
        for student in self.students:
            names.append(student.name)
            names.extend(student.descendants())
        return sorted(names)          


# In[9]:


peter = Student('Peter')
tom = Student('Tom', advisor=peter);
simon = Student('Simon', advisor=peter)
dora = Student('Dora',advisor=tom)

print(dora.ancestors()); print(peter.descendants())


#     CALCULATOR CLASS
# 
#     In this problem you should create a class Calculator implementing a
#     very simple calculator, storing an integer value. Calculator()
#     should create a new Calculator object and initialize it to store
#     the value 0.
# 
#     The class Calcuator should support the three methodds add, mult 
#     and reset. Given a Calcuator c, the three methods should
# 
#       c.add(x)   # add x to the value stored in c
#       c.mult(x)  # multiply the value stored in c by x
#       c.reset()  # reset the value stored in c to 0
# 
#     Each of the three methods should return the new value stored in
#     the Calculator c.
# 
#     An example usage of the class Calculator could be
# 
#       c = Calculator()
#       print(c.add(7))
#       print(c.mult(6))
#       print(c.reset())
#       print(c.add(1))
#       print(c.add(2))
#       print(c.add(3))
# 
#     that should print the values
# 
#       7
#       42
#       0
#       1
#       3
#       6
# 
#     Input:  
# 
#       A Python expression using the Calculator class.
# 
#     Output: 
# 
#       The result of evaluation the expression.
# 
#     Example:
# 
#       Input:  [x for c in [Calculator()] for x in [c.add(7), c.mult(6), c.reset(), c.add(1), c.add(2), c.add(3)]]
# 
#       Output: [7, 42, 0, 1, 3, 6]
# 
#     Note:
# 
#       The below code already takes care of the input and output. 
#       Your only task is to implement the methods in the
#       class Calculator.

# In[ ]:


class CALCULATOR:
    def __init__(self):
        self.value = 0
        
    def reset():
        

