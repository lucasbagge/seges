#!/usr/bin/env python
# coding: utf-8

# # Learning Pytorch
# 
# * [Youtube video side](https://www.youtube.com/watch?v=V_xro1bcAuA&t=40s)
# * [Kode](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1hUcDlKNFBOaVJPMHh5WTBGSUdzVm5zaHlfUXxBQ3Jtc0ttVWh5OUhGSGtON1ZyRkZJcXM3TGtrSmV6eUIyckRlQU1fX2xLVDN1VDJkMkgtVHg4QmJyUE14NjdBVzh1MGVLR01MSWV6WGVmSzhTc3JjWm9aVkV3T01TN3hua1NaWDVlUWYxUlowUGE0RGRMVjZ2SQ&q=https%3A%2F%2Fgithub.com%2Fmrdbourke%2Fpytorch-deep-learning&v=V_xro1bcAuA)
# * [learnpytorch](https://www.learnpytorch.io)

# In[1]:


get_ipython().system('nvidia-smi')


# In[2]:


import torch
import pandas as pd
import numpy as np
print(torch.__version__)


# # Tesnor
# 
# Måden at repræsenter data på. 
# 
# * Skalar tensor, 
# * Vector
#   * Husk at forskellen mellem dimension og shape 
# * Random tensor er vigtig da Neural netværk starter med tilfældige tal men som så finder et mønster. 

# In[14]:


scalar = torch.tensor(7)
vector = torch.tensor([7, 7])

random_tensro = torch.rand(3, 4)

print('Dimension af skalar \n', scalar.ndim)
print('items af skalar \n', scalar.item())

print('vector af skalar \n', vector)
print('vector af dimension \n', vector.ndim)

print('random \n', random_tensro)


# In[15]:


# zero
zeroas = torch.zeros(size = (3, 4))
zeroas


# vigtig at tensor har rette type, shape og device (om cuda, cpu eller gpu)

# # Pytorch workflow
# 

# In[30]:


import torch
from torch import nn
import matplotlib.pyplot as plt


# In[21]:


get_ipython().system('pip install matplotlib')


# # Data (preparing and loading)
# 
# Lav data *know* with used of linear regression

# In[46]:


from pyparsing import srange


weights = 0.7
bias = 0.3

start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1) # unsqueeze tilføjer en dimension.
y = weights * X + bias

X[:10], y[:10]


# In[25]:


len(X), len(y)


# In[27]:


# Splitting into 
train_split = int(0.8 * len(X))

X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

len(X_train), len(X_test)


# In[31]:


def plot_predictions(train_data = X_train,
                     train_labels = y_train,
                     test_data = X_test,
                     test_labels = y_test,
                     predictions = None):
    """_summary_

    Args:
        train_data (_type_, optional): _description_. Defaults to X_train.
        train_labels (_type_, optional): _description_. Defaults to y_train.
        test_data (_type_, optional): _description_. Defaults to X_test.
        test_labels (_type_, optional): _description_. Defaults to y_test.
        predictions (_type_, optional): _description_. Defaults to None.
    """
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c = 'b', s = 4, label = 'Training Data')
    
    plt.scatter(test_data, test_labels, c = 'g', s = 4, label = 'Test Data')
    
    if predictions != None:
        plt.scatter(test_data, predictions, c = 'r', s = 4, label = 'Predictions')
        
    plt.legend(prop = {'size': 14}); 


# In[32]:


plot_predictions()


# In[53]:


# Build model
## Laver inheriant form nn.Module. Der indeholder en masse
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, 
                                                requires_grad=True,
                                                dtype = torch.float))
        self.bias = nn.Parameter(torch.randn(1,
                                             requires_grad=True,
                                             dtype = torch.float))
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias


# What is super()?
# 
# * It 
# 
# 

# # Main classes
# 
# * torch.nn -> neruale netværk
# * torch.Parameter -> ting vi vil lære
# * torch.nn.Moduel -> Base klassen for alle neurale netværk. 
# * torch.optim -> optimerings algoritmer.
# * def forward() -> Alle nn.Module kræver vi skal overskride forward. Den definer hvad der ske ri forward beregningen.

# In[40]:


torch.randn(1)


# In[55]:


# Se output for modellen vi har lavet

## Random seed

torch.manual_seed(42)

model_0 = LinearRegressionModel()

# Tjek parameterne
list(model_0.parameters())


# In[44]:


# List named parameter

model_0.state_dict()


# In[47]:


weights, bias 


# # Making prediction with `torch.inference_mode()`
# 
# 

# In[59]:


# Inference mode is a content manager and is important
# We loose the tracking of other things so we can keep things faster. 

y_preds2 = model_0(X_test)
y_preds2


# In[56]:


with torch.inference_mode():
    y_preds = model_0(X_test)

y_preds


# In[57]:


y_test


# In[58]:


plot_predictions(predictions=y_preds)


# In[ ]:




