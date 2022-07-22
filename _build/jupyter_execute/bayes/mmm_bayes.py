#!/usr/bin/env python
# coding: utf-8

# # Media Mixed Modelling with Bayesian statistics

# In[1]:


# use poetry add `cat requirements.txt` for installain in req
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import pymc3 as pm
import seaborn as sns

plt.style.use("bmh")
plt.rcParams["figure.figsize"] = [10, 6]
plt.rcParams["figure.dpi"] = 100


# In[2]:


spend_data = pd.read_excel('../data/mmm data.xlsx')

spend_data.head()


# In[3]:


plt.plot(spend_data['channel_1'])
plt.plot(spend_data['channel_2'])
plt.plot(spend_data['channel_3'])
plt.plot(spend_data['channel_4'])
plt.plot(spend_data['channel_5'])
plt.plot(spend_data['channel_6'])


# In[4]:


sales = (20 + spend_data['channel_1'] * 1.1 + spend_data['channel_2'] * 0.7 + 
         spend_data['channel_3'] * 0.8 + spend_data['channel_4'] *1.5 + 
         spend_data['channel_5'] * 0.8 + spend_data['channel_6'] * 0.95 +
         np.random.normal(20, 5, size=len(spend_data['channel_1']))
  )

sales = spend_data['sales'] # Use this to replicate my results exactly
spend_data = spend_data.drop('sales', axis=1)


# In[5]:


spend_data.head()


# In[6]:


sales


# In[7]:


spend_data_with_c = sm.add_constant(spend_data)
est = sm.OLS(sales, spend_data_with_c).fit()
est.summary()


# In[8]:


with pm.Model() as model:
    sigma = pm.HalfNormal("sigma", sigma=1)
    intercept = pm.Normal("Intercept", 0, sigma=20)
    beta = pm.Normal("x", 0, sigma=20, shape = 6)
    mu = intercept + beta[0] * spend_data['channel_1']                    + beta[1] * spend_data['channel_2']                    + beta[2] * spend_data['channel_3']                    + beta[3] * spend_data['channel_4']                    + beta[4] * spend_data['channel_5']                    + beta[5] * spend_data['channel_6']

    # Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=sales)

    # pm.glm.GLM.from_formula("y ~ x", data)
    ols_trace = pm.sample(2000, cores=2)


# In[9]:


ols_trace_df = pm.trace_to_dataframe(ols_trace)
res = ols_trace_df.describe().filter(['mean'],axis=0).T
res.index=['Intercept', 'beta_1', 'beta_2', 'beta_3', 'beta_4', 'beta_5', 'beta_6', 'sigma']
res


# In[11]:


with pm.Model() as model:
    sigma = pm.HalfNormal("sigma", sigma=1)
    intercept = pm.Normal("Intercept", 0, sigma=20)
    BoundedNormal = pm.Bound(pm.Normal, lower=0.0)
    beta = BoundedNormal("x", 0, sigma=20, shape = 6)
    mu = intercept + beta[0] * spend_data['channel_1']                    + beta[1] * spend_data['channel_2']                    + beta[2] * spend_data['channel_3']                    + beta[3] * spend_data['channel_4']                    + beta[4] * spend_data['channel_5']                    + beta[5] * spend_data['channel_6']

    # Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=sales)


    # pm.glm.GLM.from_formula("y ~ x", data)
    bounded_trace = pm.sample(2000, cores=2)


# In[12]:


bounded_trace_df = pm.trace_to_dataframe(bounded_trace)
res= bounded_trace_df.describe().filter(['mean'],axis=0).T
res.index=['Intercept', 'beta_1', 'beta_2', 'beta_3', 'beta_4', 'beta_5', 'beta_6', 'sigma']
res


# In[13]:


bt_means = bounded_trace_df[['Intercept','x__0','x__1','x__2','x__3','x__4', 'x__5']].mean().values
ols_means = ols_trace_df[['Intercept','x__0','x__1','x__2','x__3','x__4', 'x__5']].mean().values


# In[14]:


pd.DataFrame({'Truth':np.array([20, 1.1, 0.7, 0.8, 1.5, 0.8, 0.95]), 'ols':est.params, 'bayes_ols':ols_means, 'bounded':bt_means})


# In[ ]:




