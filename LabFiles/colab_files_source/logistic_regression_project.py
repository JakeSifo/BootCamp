
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

input_file = 'http://bit.ly/2O7Islk'
df = pd.read_csv(input_file, header=None, sep=',')
y = df[57]
X = df.iloc[:,:-1]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=11)
print (X_train.shape, X_test.shape)

logit = LogisticRegression() 

logit.fit(X_train, y_train)

# Increase the max_iter parameter
logit = LogisticRegression( max_iter=2000)

logit.fit(X_train, y_train)

y_pred = logit.predict(X_test)
confusion_matrix(y_test, y_pred)

logit = LogisticRegression(max_iter=2000, C=0.5)

logit.fit(X_train, y_train)
y_pred = logit.predict(X_test)
confusion_matrix(y_test, y_pred)

logit = LogisticRegression(max_iter=2000, C=3)
logit.fit(X_train, y_train)

# Increase the max_iter parameter
logit = LogisticRegression(max_iter=2 * 2000, C=3)
logit.fit(X_train, y_train)

y_pred = logit.predict(X_test)
confusion_matrix(y_test, y_pred)


import pickle
pkl_file = "logit.pkl"
with open(pkl_file, "wb") as fout:
  pickle.dump(logit,fout)

import os
for f in os.scandir():
  if f.name == pkl_file:
    print(pkl_file, f.stat().st_size)

