#!/usr/bin/env python
# coding: utf-8

# # ML
# 
# ML is the way a program learn something with only data as input. 
# 
# Today there is multiple examples of ML where you classify spam or try to forecast
# 
# 
# Got It!
# 1. Machine learning with scikit-learn
# Hi, and welcome! My name is George Boorman, and I'll be your instructor for this course on supervised learning with scikit-learn.
# 
# 2. What is machine learning?
# Machine learning is the process whereby computers learn to make decisions from data without being explicitly programmed.
# 
# 3. Examples of machine learning
# For example, learning to predict whether an email is spam or not spam given its content and sender. Or learning to cluster books into different categories based on the words they contain, then assigning any new book to one of the existing clusters.
# 
# 4. Unsupervised learning
# Unsupervised learning is the process of uncovering hidden patterns and structures from unlabeled data. For example, a business may wish to group its customers into distinct categories based on their purchasing behavior without knowing in advance what these categories are. This is known as clustering, one branch of unsupervised learning.
# 
# 5. Supervised learning
# Supervised learning is a type of machine learning where the values to be predicted are already known, and a model is built with the aim of accurately predicting values of previously unseen data. Supervised learning uses features to predict the value of a target variable, such as predicting a basketball player's position based on their points per game. This course will exclusively focus on supervised learning.
# 
# 6. Types of supervised learning
# There are two types of supervised learning. Classification is used to predict the label, or category, of an observation. For example, we can predict whether a bank transaction is fraudulent or not. As there are two outcomes here - a fraudulent transaction, or non-fraudulent transaction, this is known as binary classification. Regression is used to predict continuous values. For example, a model can use features such as number of bedrooms, and the size of a property, to predict the target variable, price of the property.
# 
# 7. Naming conventions
# Note that what we call a feature throughout the course, others may call a predictor variable or independent variable. Also, what we call the target variable, others may call dependent variable or response variable.
# 
# 8. Before you use supervised learning
# There are some requirements to satisfy before performing supervised learning. Our data must not have missing values, must be in numeric format, and stored as pandas DataFrames or Series, or NumPy arrays. This requires some exploratory data analysis first to ensure data is in the correct format. Various pandas methods for descriptive statistics, along with appropriate data visualizations, are useful in this step.
# 
# 9. scikit-learn syntax
# scikit-learn follows the same syntax for all supervised learning models, which makes the workflow repeatable. Let's familiarize ourselves with the general scikit-learn workflow syntax, before we explore using real data later in the chapter. We import a Model, which is a type of algorithm for our supervised learning problem, from an sklearn module. For example, the k-Nearest Neighbors model uses distance between observations to predict labels or values. We create a variable named model, and instantiate the Model. A model is fit to the data, where it learns patterns about the features and the target variable. We fit the model to X, an array of our features, and y, an array of our target variable values. We then use the model's dot-predict method, passing six new observations, X_new. For example, if feeding features from six emails to a spam classification model, an array of six values is returned. A one indicates the model predicts that email is spam, and a zero represents a prediction of not spam.

# 
# Got It!
# 1. The classification challenge
# Previously, we learned that supervised learning uses labels. Let's discuss how we can build a classification model, or classifier, to predict the labels of unseen data.
# 
# 2. Classifying labels of unseen data
# There are four steps. First, we build a classifier, which learns from the labeled data we pass to it. We then pass it unlabeled data as input, and have it predict labels for this unseen data. As the classifier learns from the labeled data, we call this the training data.
# 
# 3. k-Nearest Neighbors
# Let's build our first model! We'll use an algorithm called k-Nearest Neighbors, which is popular for classification problems. The idea of k-Nearest Neighbors, or KNN, is to predict the label of any data point by looking at the k, for example, three, closest labeled data points and getting them to vote on what label the unlabeled observation should have. KNN uses majority voting, which makes predictions based on what label the majority of nearest neighbors have.
# 
# 4. k-Nearest Neighbors
# Using this scatter plot as an example, how do we classify the black observation?
# 
# 5. k-Nearest Neighbors
# If k equals three, we would classify it as red. This is because two of the three closest observations are red.
# 
# 6. k-Nearest Neighbors
# If k equals five, we would instead classify it as blue.
# 
# 7. KNN Intuition
# To build intuition for KNN, let's look at this scatter plot displaying total evening charge against total day charge for customers of a telecom company. The observations are colored in blue for customers who have churned, and red for those who have not churned.
# 
# 8. KNN Intuition
# Here we have visualized the results of a KNN algorithm where the number of neighbors is set to 15. KNN creates a decision boundary to predict if customers will churn. Any customers in the area with a gray background are predicted to churn, and those in the area with a red background are predicted to not churn. This boundary would be used to make predictions on unseen data.
# 
# 9. Using scikit-learn to fit a classifier
# To fit a KNN model using scikit-learn, we import KNeighborsClassifier from sklearn-dot-neighbors. We split our data into X, a 2D array of our features, and y, a 1D array of the target values - in this case, churn status. scikit-learn requires that the features are in an array where each column is a feature and each row a different observation. Similarly, the target needs to be a single column with the same number of observations as the feature data. We use the dot-values attribute to convert X and y to NumPy arrays. Printing the shape of X and y, we see there are 3333 observations of two features, and 3333 observations of the target variable. We then instantiate our KNeighborsClassifier, setting n_neighbors equal to 15, and assign it to the variable knn. Then we can fit this classifier to our labeled data by applying the classifier's dot-fit method and passing two arguments: the feature values, X, and the target values, y.
# 
# 10. Predicting on unlabeled data
# Here we have a set of new observations, X_new. Checking the shape of X_new, we see it has three rows and two columns, that is, three observations and two features. We use the classifier's dot-predict method and pass it the unseen data as a 2D NumPy array containing features in columns and observations in rows. Printing the predictions returns a binary value for each observation or row in X_new. It predicts 1, which corresponds to 'churn', for the first observation, and 0, which corresponds to 'no churn', for the second and third observations.
# 
# 11. Let's practice!
# Now let's build our own KNN model for the churn dataset, which we will use for the remainder of the chapter!
