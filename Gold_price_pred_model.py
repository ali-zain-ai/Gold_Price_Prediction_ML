import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt
# import seaborn as sns

data_set = pd.read_csv(r"D:\AI_Python\Gold Price Prediction\gld_price_data.csv")

# print(data_set.head(10))
# print(data_set.tail(10))
# print(data_set.shape)
# print(data_set.info())
# print(data_set.describe())

# Positive and Negative Correlation
X = data_set.drop(columns=['Date', 'GLD'], axis=1)
# print(X)

Y = data_set['GLD']

X_train, X_test, Y_train, Y_test = (train_test_split(X, Y, test_size=0.2, random_state=1))

#Model training 
model = RandomForestRegressor(max_depth=3)
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

accuracy = r2_score(Y_test, y_pred)
print(accuracy)
print(f"Model Accuracy = {accuracy*100:.2f}%")

