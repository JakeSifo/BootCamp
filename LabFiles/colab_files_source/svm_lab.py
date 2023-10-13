# -*- coding: utf-8 -*-
"""The SVM Lab

Automatically generated by Colaboratory.

"""

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

input_file = 'http://bit.ly/2O7Islk'
df = pd.read_csv(input_file, header=None, sep=',')
df.head()

y = df[57]
X = df.iloc[:,:-1]

X.shape, df.shape

X = preprocessing.MinMaxScaler(feature_range=(-1,1)).fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=11)
print (X_train.shape, X_test.shape)

y_train[:20]

"""## Train the Model"""

lsvm_model = svm.LinearSVC(max_iter=2500, random_state=11)
lsvm_model.fit(X_train, y_train)

y_predicted = lsvm_model.predict(X_test)

confusion_matrix(y_test, y_predicted)

lsvm_model.score(X_train, y_train)
# RF: 1.0

lsvm_model.score(X_test, y_test)
# RF: 0.9500362056480811

"""GridSearchCV"""

from sklearn.model_selection import GridSearchCV
# Check the RAM parameter (RAM Disk) in the top right corner of the screen
ca_si_MB  = 1_024   # 1 GB
svc_GSCV = svm.SVC (cache_size=ca_si_MB)
print(svc_GSCV)

import os; os.cpu_count()

parameters = {'kernel':('linear', 'rbf'), 'C':[0.1, 0.5, 1, 5, 10]} 
svm_grid = GridSearchCV( 
        svc_GSCV, 
        param_grid= parameters, 
        refit = True,  
        n_jobs = -1,  
        cv = 10)  

print (svm_grid)

svm_grid.fit (X_train, y_train)

best_e= svm_grid.best_estimator_; best_e

best_e.score(X_train, y_train), best_e.score(X_test, y_test)

y_pred_2 = best_e.predict(X_test)
confusion_matrix(y_test, y_pred_2)

"""```
RandomForest lab:
array([[802,  20],
       [ 49, 510]])


```
"""


best_e2= svm_grid2.best_estimator_; best_e2

best_e2.score(X_train, y_train), best_e.score(X_test, y_test)

y_pred_3 = best_e2.predict(X_test)
confusion_matrix(y_test, y_pred_3)

