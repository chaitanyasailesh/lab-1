from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# importing the data set
data_set = pd.read_csv('wineQR.csv')
# EDA
print(data_set['quality'].value_counts(dropna='False'))
# searching for attributes which have null values
nulls = pd.DataFrame(data_set.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
print(nulls)
numeric_features = data_set.select_dtypes(include=[np.number])
corr = numeric_features.corr()
# correlation
print(corr['quality'].sort_values(ascending=False)[:4])
data_set['density'].fillna((data_set['density'].mean()), inplace=True)
print(data_set["density"].isnull().any())
data_set['free.sulfur.dioxide'].fillna((data_set['free.sulfur.dioxide'].mean()), inplace=True)
print(data_set["free.sulfur.dioxide"].isnull().any())

X_train, X_test = train_test_split(data_set, test_size=0.2)
y_train = X_train['quality']

X_train = X_train.drop(columns=['quality'])
y_test = X_test['quality']
X_test = X_test.drop(columns=['quality'])
# create regression model and train it
reg = LinearRegression().fit(X_train, y_train)


prediction = reg.predict(X_test)
# evaluating the required models by metrics
mean_squared_error = mean_squared_error(y_test, prediction)
r2_score = r2_score(y_test, prediction)
# rmse(measures the differences between values predicted by a model)
# r2(regression score function)
print("mean squared error is :", mean_squared_error)
print("r2_score is: ", r2_score)