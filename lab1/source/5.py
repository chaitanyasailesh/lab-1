import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import warnings

warnings.filterwarnings("ignore")
# importing the data set
data_set = pd.read_csv('housing.csv')
# encoding the categorical features
data_set = data_set.apply(LabelEncoder().fit_transform)
# EDA
print(data_set['ocean_proximity'].value_counts(dropna='False'))
# searching for attributes which have null values
nulls = pd.DataFrame(data_set.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
print(nulls)
numeric_features = data_set.select_dtypes(include=[np.number])
corr = numeric_features.corr()
# correlation of best features respected to target class
print(corr['ocean_proximity'].sort_values(ascending=False)[:4])
# replacing with mean
data_set['total_bedrooms'].fillna((data_set['total_bedrooms'].mean()), inplace=True)
print(data_set["total_bedrooms"].isnull().any())
data_set['households'].fillna((data_set['households'].mean()), inplace=True)
print(data_set["households"].isnull().any())
# training set
X = data_set.drop('ocean_proximity', axis=1)
y = data_set.iloc[:, 9].values
# Splitting the data into Training and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=20)

# Scaling the values
from sklearn.preprocessing import StandardScaler
scalar_X = StandardScaler()
X_train = scalar_X.fit_transform(X_train)
X_test = scalar_X.transform(X_test)

# Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)
y_pred1 = model.predict(X_test)
accuracy_1 = metrics.accuracy_score(y_test, y_pred1)
print("Gaussian Naive Bayes accuracy :", accuracy_1)

# SVM
clf = SVC(kernel='linear', C=1).fit(X_train, y_train)
y_pred2 = clf.predict(X_test)
accuracy_2 = metrics.accuracy_score(y_test, y_pred2)
print("svm accuracy :", accuracy_2)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred3 = knn.predict(X_test)
accuracy_3 = metrics.accuracy_score(y_test, y_pred3)
print("KNN accuracy :", accuracy_3)



