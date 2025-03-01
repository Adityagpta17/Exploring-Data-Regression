import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random

# Read the data
data = pd.read_csv("E:\\python_\\diabetes.csv")

# Define features and target variable
X = data[['Glucose']]
Y = data[['Outcome']]

# Seed for reproducibility
random.seed(1)

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

# Create and train the model
log_reg = LogisticRegression()
log_reg.fit(X_train, Y_train)

# Print the score
print(log_reg.score(X_test, Y_test))
