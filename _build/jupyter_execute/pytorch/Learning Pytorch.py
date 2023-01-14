#!/usr/bin/env python
# coding: utf-8

# # Learning Pytorch
# 
# * [Youtube video side](https://www.youtube.com/watch?v=V_xro1bcAuA&t=40s)
# * [Kode](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1hUcDlKNFBOaVJPMHh5WTBGSUdzVm5zaHlfUXxBQ3Jtc0ttVWh5OUhGSGtON1ZyRkZJcXM3TGtrSmV6eUIyckRlQU1fX2xLVDN1VDJkMkgtVHg4QmJyUE14NjdBVzh1MGVLR01MSWV6WGVmSzhTc3JjWm9aVkV3T01TN3hua1NaWDVlUWYxUlowUGE0RGRMVjZ2SQ&q=https%3A%2F%2Fgithub.com%2Fmrdbourke%2Fpytorch-deep-learning&v=V_xro1bcAuA)
# * [learnpytorch](https://www.learnpytorch.io)

# In[1]:


import torch
import pandas as pd
import numpy as np


# # Tesnor
# 
# Måden at repræsenter data på. 
# 
# * Skalar tensor, 
# * Vector
#   * Husk at forskellen mellem dimension og shape 
# * Random tensor er vigtig da Neural netværk starter med tilfældige tal men som så finder et mønster. 

# In[ ]:


scalar = torch.tensor(7)
vector = torch.tensor([7, 7])

random_tensro = torch.rand(3, 4)

print('Dimension af skalar \n', scalar.ndim)
print('items af skalar \n', scalar.item())

print('vector af skalar \n', vector)
print('vector af dimension \n', vector.ndim)

print('random \n', random_tensro)


# In[ ]:


# zero
zeroas = torch.zeros(size = (3, 4))
zeroas


# vigtig at tensor har rette type, shape og device (om cuda, cpu eller gpu)

# # Pytorch workflow
# 

# In[ ]:


import torch
from torch import nn
import matplotlib.pyplot as plt


# # Data (preparing and loading)
# 
# Lav data *know* with used of linear regression

# In[ ]:


from pyparsing import srange


weights = 0.7
bias = 0.3

start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1) # unsqueeze tilføjer en dimension.
y = weights * X + bias

X[:10], y[:10]


# In[ ]:


len(X), len(y)


# In[ ]:


# Splitting into 
train_split = int(0.8 * len(X))

X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

len(X_train), len(X_test)


# In[ ]:


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


# In[ ]:


plot_predictions()


# In[ ]:


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

# In[ ]:


torch.randn(1)


# In[ ]:


# Se output for modellen vi har lavet

## Random seed

torch.manual_seed(42)

model_0 = LinearRegressionModel()

# Tjek parameterne
list(model_0.parameters())


# In[ ]:


# List named parameter

model_0.state_dict()


# In[ ]:


weights, bias 


# # Making prediction with `torch.inference_mode()`
# 
# 

# In[ ]:


# Inference mode is a content manager and is important
# We loose the tracking of other things so we can keep things faster. 

y_preds2 = model_0(X_test)
y_preds2


# In[ ]:


with torch.inference_mode():
    y_preds = model_0(X_test)

y_preds


# In[ ]:


plot_predictions(predictions=y_preds)


# ## Train model
# 
# Mening er vi kommer til at kende de ukendte variabler. 
# 
# VI kan træner loss og optimizer
# 
# 

# In[ ]:


list(model_0.parameters())


# In[ ]:


model_0.state_dict()


# In[ ]:


# Setup loss
loss_fn = nn.L1Loss()

# Setup optimizer
optimizer = (
    torch
    .optim
    .SGD(params = model_0.parameters(),
                            lr = 0.01) # Ændre på vægten men hvor deciamlen er den so ændres.
)


# ## Traning loop for optimize parameter
# 
# 0. loop thoug data
# 1. forward pass also calle dforward propagation
# 2. calculate loss (compar forward pass prediction to ground truth)
# 3. optimize zero grad
# 4. loss backward - move backward to calculat ethe gradients 
# 5. optimizer step - adjust paramrter
# 
# * E

# In[ ]:


torch.manual_seed(123)



# loop though the data (because we set epochs ourselves it is a hyperparameter)
epochs = 200

epochs_count = []
loss_values = []
test_loss_value = []

# 0. loop though data

for epoch in range(epochs):
    # Set the model to traning mode. Make sure that we update gradients. 
    model_0.train()
    
    # 1. forwars
    y_pred = model_0(X_train)
    
    # 2. loss
    loss = loss_fn(y_pred, y_train)
    print(f'Loss:', {loss})
    
    # 3. Optimize 
    optimizer.zero_grad()
    
    # 4. Perform backpropagation
    loss.backward()
    
    # 5. OPtimizer performance
    optimizer.step()
    
    ### Testing
    model_0.eval()  # Turn gradients off. Husk at gøre det når vi tester modellen. 
    with torch.inference_mode(): # Turns of gradients tracking and other things
        # 1. forward pass
        test_pred = model_0(X_test)
        # 2. Loss
        test_loss = loss_fn(test_pred, y_test)
        # 3. Optimize
        
    # Print out
    if epoch % 40 == 0:
        epochs_count.append(epoch)
        loss_values.append(loss)
        test_loss_value.append(test_loss)
        print(f'Epoch:  {epoch} | Test {loss} | Test loss {test_loss}')
        print(model_0.state_dict())    


# In[ ]:


weights, bias


# In[ ]:


test_loss_value


# In[ ]:


# Plot loss
plt.plot(epochs_count, torch.tensor(loss_values).numpy(), label = 'Train loss')
plt.plot(epochs_count, test_loss_value, label = "Test loss")
plt.title('Train and Test loss curve')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend();


# In[ ]:


with torch.inference_mode():
    y_preds_new = model_0(X_test)


# In[ ]:


plot_predictions(predictions=y_preds_new)


# ## Save model
# 
# 3 metoder til saving and loading models
# 
# 1. `torch.save()` - save in pickle format. 
# 2. `torch.load()` 
# 3. `torch.nn.Module.load_stat_dict()` - load state dict

# In[ ]:


# Saves models output in a python dict. 
model_0.state_dict()


# In[ ]:


from pathlib import Path

# 1. Lav folder til model
MODEL_PATH = Path('models')
MODEL_PATH.mkdir(parents = True, exist_ok=True)

# 2. Lav model save path
MODEL_NAME = '01_pytorch_wf_model_0.pth'
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME
MODEL_SAVE_PATH
 
# 3. Gem model state dict
torch.save(obj = model_0.state_dict(), 
           f = MODEL_SAVE_PATH)


# In[ ]:


# Load 
loaded_model_0 = LinearRegressionModel()

# Load state dict
loaded_model_0.load_state_dict(torch.load(f=MODEL_SAVE_PATH))

print(f'Load model with weight \n: {loaded_model_0.state_dict()}')


# In[ ]:


# Make predictions

loaded_model_0.eval()
with torch.inference_mode():
    y_pred_load_model_0 = loaded_model_0(X_test)

y_pred_load_model_0    


# In[ ]:


torch.__version__


# ## Data
# 
# Create device agnostic code. 
# If GPU then we use it. This will do we get a faster computer. 

# In[ ]:


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'this is {device}')


# # Chapter 2 – Neural Network Classification
# 
# * Imagenet: Famouse multi classification dataset. 
# * Batch size: 32 is a ideal choize. Measning if a classification look at a image it will look at 32 picture. 
# 
# ## Archeticure of NNE
# 
# Input layer: Is number of features
# Hidden Layer: are math stages in the framework. 
# Loss: Measure how wrong our model is.
# 
# ## 1. Make Data ready

# In[1]:


import sklearn


# In[3]:


from sklearn.datasets import make_circles

n_samples = 1000

X, y = make_circles(n_samples,
                    noise = 0.03,
                    random_state = 42)

len(X), len(y)


# In[4]:


print(X[:5]), print(y[:5])


# In[5]:


# Make DF with Pandas

import pandas as pd
circles = pd.DataFrame({'X1': X[:, 0], 
                        "X2": X[:, 1],
                       "label": y })
circles


# In[6]:


# Visual

import matplotlib.pyplot as plt

plt.scatter(x = X[:, 0],
            y = X[:, 1],
            c = y,
            cmap = plt.cm.RdBu);


# We want to differentiae between the two circles. 
# 
# * Binary classification. 

# In[7]:


X_sample = X[0]
y_sample = y[0]

X_sample, y_sample


# In[8]:


# Train and test

import torch


# In[9]:


X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)

X[:5], y[:5]


# In[10]:


X.dtype


# In[11]:


# Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

len(X_train), len(X_test)


# In[12]:


device = 'cuda' if torch.cuda.is_available() else 'cpu'
device


# In[13]:


from torch import nn
## Building model

class CircleModelsv0(nn.Module):
    
    def __init__(self):
        super().__init__()
        
    # 2. Create 2 nn.Linear layer to handle shape
    ## The `out_features` need to have the same shap af y which is 1.
    ## nn.Linear transfor as acording to https://pytorch.org/docs/stable/generated/torch.nn.Linear.html
        self.layer_1 = nn.Linear(in_features=2, out_features=5)
    # The second layer need to mach the out_features of first layer. 
        self.layer_2 = nn.Linear(in_features=5, out_features=1) # Tak 5 feature and output 1 feature same shape as y
    
    # 3. define forward
    def forward(self, x):
        return self.layer_2(self.layer_1(x) ) # x->layer_1 -> layer_2 -> output
    
    # 4. Instanit instance of model.
    
model_0 = CircleModelsv0().to(device)
model_0


# In[14]:


# Using nn.Sequential

## Building model

class CircleModelsv0(nn.Module):
    
    def __init__(self):
        super().__init__()
        
    # 2. Create 2 nn.Linear layer to handle shape
    ## The `out_features` need to have the same shap af y which is 1.
    ## nn.Linear transfor as acording to https://pytorch.org/docs/stable/generated/torch.nn.Linear.html
        self.layer_1 = nn.Linear(in_features=2, out_features=5)
    # The second layer need to mach the out_features of first layer. 
        self.layer_2 = nn.Linear(in_features=5, out_features=1) # Tak 5 feature and output 1 feature same shape as y
    
    # 3. define forward
    def forward(self, x):
        return self.layer_2(self.layer_1(x) ) # x->layer_1 -> layer_2 -> output
    
    # 4. Instanit instance of model.
    
model_0 = CircleModelsv0().to(device)
model_0


# In[26]:


# Dont define forward like before. 
mode_0 = nn.Sequential(
    nn.Linear(in_features=2, out_features=5),
    nn.Linear(in_features=5, out_features=1)
).to(device)

mode_0


# It is esier but when more complex, then it is good we can build our own layers. 
# 
# A Sequential can be used inside class. 

# In[27]:


model_0.state_dict()


# Get weights now

# In[25]:


# Predictions

untrained_preds = model_0(X_test.to(device))
print(f'Length of pred: {len(untrained_preds)}, shape {untrained_preds.shape}')


# In[ ]:




