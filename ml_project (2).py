# -*- coding: utf-8 -*-
"""ML Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_XU_nI-a-UDA8wixQ8c47B0T7M8UiXr
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  8, 10, 12, 14, 16, 18, 20]
plt.scatter(height,weight,color='black')
plt.xlabel("height")
plt.ylabel("weight")
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[11.0]]
print(reg.predict(X_height))

#import modules
import warnings
import pandas as pd
from sklearn import model_selection
import numpy as np
import sklearn
from sklearn import linear_model
X=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
y=[  8, 10 , 12, 14, 16, 18, 20]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=7)
print("Training Features", X_train);print("Training Labels",y_train);print("Training Data",X_test);print("Testing Data",y_test)
reg=linear_model.LinearRegression()
reg.fit(X_train,y_train)
#accuracy on test set
result = reg.score(X_test, y_test)
print("Accuracy - test set: %.2f%%" % (result*100.0))
X_height=[[12.0]]
print(reg.predict(X_test))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X,y)
X_marks=[[80]]
print(classifier.predict(X_marks))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
from sklearn.neighbors import KNeighborsClassifier  
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )  
classifier.fit(X,y) 
X_marks=[[20]]
print(classifier.predict(X_marks))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(X,y)
X_marks=[[70]]
print(RandomForestRegModel.predict(X_marks))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X,y)
X_marks=[[55]]
print(classifier.predict(X_marks))

import numpy as np
import pandas as pd
from google.colab import files
uploaded = files.upload()
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("diabetes.csv.xls")
df.head()
x=df.drop('diabetes',axis=1)
y=df['diabetes']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
model=GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
y_pred

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeRegressor

x = [[10],[20],[30],[40],[50],[60],[70]]
y = [[0],[0],[0],[1],[1],[1],[1]]

plt.scatter(x, y, color='black')
plt.xlabel("x")
plt.ylabel("y")

reg = DecisionTreeRegressor()  # Use DecisionTreeRegressor instead of LinearRegression
reg.fit(x, y)

x_ = [[12.0]]
print(reg.predict(x_))