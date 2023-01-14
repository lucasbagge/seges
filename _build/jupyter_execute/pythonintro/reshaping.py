#!/usr/bin/env python
# coding: utf-8

# # Reshaping By Pivoting and Grouping
# 
# This post will explore one of the most powerful options for data manipulations, pivot tables. Pandas provides multiple syntaxes for creating them. One uses the .pivot_table method, the other common one leverages the .groupby method, you can also represent some of these operations with the pd.crosstab function.

# In[1]:


import pandas as pd
pd.set_option('display.max_columns', None)

nba = pd.read_csv("nba_all_elo.csv")
nba.head(2)


# When your boss asks you to get numbers ”by X column”, that should be a hint to pivot (or group) your data. Assume your boss asked, ”What is the average age by the country for each employment status?” This is like one of those word problems that you had to learn how to do in math class, and you needed to translate the words into math operations. In this case, we need to pick a pandas operation to use and then map the problem into those operations.
# 
# These map cleanly to the parameters of the .pivot_table method. One solution would look like this:

# In[2]:


(
    nba
    .pivot_table(
        index='fran_id',
        columns='opp_id',
        values='forecast',
        aggfunc='mean'
    )
)


# It turns out that we can use the pd.crosstab function as well. Because this is a function, we need to provide the data as series rather than the column names:

# In[3]:


(
    pd.crosstab
    (
        index=nba.fran_id,
        columns=nba.opp_id,
        values=nba.forecast,
        aggfunc='mean'
    )
)


# Finally, we can do this with a .groupby method call.
# DataFrameGroupBy object. It is a lazy object and does not perform any calculations until we indicate which aggregation to perform. We can also pull off a column and then only perform an aggregation on that column instead of all of the non-grouped columns.
# 
# This operation is a little more involved. We pull off the value colum and then calculate the mean for each id and opp id group. Then we leverage .unstack to pull out the inner- most index and push it up into a column (we will dive into .unstack later). You can think of .groupby and subsequent methods as the low-level underpinnings of .pivot_table and pd.crosstab:

# In[4]:


(
    nba
    .groupby(['fran_id', 'opp_id'])
    .forecast
    .mean()
    .unstack()
)


# Many programmers and SQL analysts find the .groupby syntax intuitive, while Excel junkies
# often feel more at home with the .pivot_table method. The crosstab function works in some situations but is not as flexible. It makes sense to learn the different options. The .groupby method is the foundation of the other two, but a cross-tabulation may be more convenient.
# 
# ## Multiple Aggregations
# 
# We can get to calculate multiple values:

# In[5]:


(
    nba
    .groupby(['fran_id'])
    .forecast
    .agg([min, max])
)


# In[ ]:




