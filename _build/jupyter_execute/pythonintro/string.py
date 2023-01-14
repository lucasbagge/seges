#!/usr/bin/env python
# coding: utf-8

# # String Manipulation
# 
# String data is commonly used to hold free-form text, semi-structured text, categorical data, and data that should have another type (typically numeric or datetime). We will look at common operations of textual data.
# 
# ## Strings and Objects
# 
# Before pandas 1.0, if you stored strings in a series the underlying type of the series was object. This is unfortunate as the object type can be used for other series that have Python types in them (such as a list, a dictionary, or a custom class). Also, the object type is used for mixed types. If you have a series that has numbers and strings in it, the type is also object.
# 
# ### The .str Accessor
# 
# The object, 'string', and 'category' types have a .str accessor that provides string manipulation methods. Most of these methods are modeled after the Python string methods. If you are adept at the Python string methods, many of the pandas variants should be second nature. Here is the Python string method .lower:

# In[1]:


import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")


# In[2]:


import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")
nba.head(2)


# In[3]:


nba.fran_id.str.lower()


# In[4]:


nba.fran_id.str.capitalize()


# In[5]:


(
    nba
    .fran_id
    .str
    .startswith('Hus')
)


# In[6]:


(
    nba
    .fran_id
    .str
    .extract(r'([a-e])', expand=False)
)


# ### Searching
# 
# There are a few methods that leverage regular expressions to perform searching, replacing, and splitting.
# 
# To find all of the non alphabetic characters (disregarding space), you could use this code:

# In[7]:


(
    nba
    .fran_id
    .str
    .extract(r'([^a-z A-Z])')
)


# This returns a dataframe that has mostly missing values and by inspection is not very useful. If we collapse it into a series (with the parameter expand=False), we can chain the .value_counts method to view the count of non-missing values:

# In[8]:


(
    nba
    .fran_id
    .str
    .extract(r'([^a-z A-Z])', expand=False)
    .value_counts()
)


# ### Replacing Text
# 
# Both the series and the .str attribute have a .replace method, and these methods have overlapping functionality. If I want to replace single characters, I typically use .str.replace, but if I have complete replacements for many of the values I use .replace.
# If I wanted to replace a capital ”A” with the Unicode letter a with a ring above it, I could use this code:

# In[9]:


nba.fran_id.str.replace('H', 'Å')


# You can use a dictionary to specify complete replacements. (This is very explicit, but it might be problematic if you had 20,000 numeric values that had dashes in them, and you wanted to strip out the dashes for all 20,000 numbers. You would have to create a dictionary with all the entries, tedious work.):

# In[10]:


nba.fran_id.replace({'Huskies': 'Åuskies', 'Knicks': 'Ånicks'})[0:2]


# Alternatively, you can specify that you mean to use a regular expression to replace just a portion of the strings with the regex=True parameter:

# In[11]:


nba.fran_id.replace('H|K', 'Å', regex=True)[0:2]


# A importance note is:
# 
# > I use .str.replace to replace substrings, and .replace to replace mappings of complete strings.
