# -*- coding: utf-8 -*-
"""Random Forest Lab

Automatically generated by Colaboratory.

"""

import numpy as np
import pandas as pd

import urllib.request as webreq
import os

local_files =  ["./training_two_classes.svm", "./test_two_classes.svm"]

urls = ['http://bit.ly/37FTdmY', 'http://bit.ly/2tLzzqV']

for f_name, url in zip(local_files, urls):
    if not os.path.exists (f_name):
        http_msg = webreq.urlretrieve (url, f_name)

from sklearn.datasets import load_svmlight_file
trainData, trainLabels = load_svmlight_file("training_two_classes.svm")

trainLabels

trainData

type(trainData)

from sklearn.ensemble import RandomForestClassifier

RFModel = RandomForestClassifier(n_estimators=3, random_state=1).fit(trainData, trainLabels)

RFModel

RFModel.estimators_

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
from sklearn import tree

plt.figure(figsize=(12,12))

tree.plot_tree(RFModel.estimators_[0], class_names= ['A', 'B']);

tree.plot_tree(RFModel.estimators_[1], class_names= ['A', 'B']);

RFModel.predict([[0,0], [10,9], [2,5], [19,18], [15,16]])

testData, testLabels = load_svmlight_file("test_two_classes.svm")

testData.toarray()

testLabels

predictedLabels = RFModel.predict(testData)

import sklearn.metrics as metrics
metrics.confusion_matrix(testLabels, predictedLabels)

testLabels[-1] = 0; testLabels

metrics.confusion_matrix(testLabels, predictedLabels)

"""## Predicting Spam """

input_file = 'http://bit.ly/2O7Islk'
df = pd.read_csv(input_file, header=None, sep=',')

df.head(), df.tail()

df.iloc[:,:-1].head()

df.iloc[:,-1].head(), df.iloc[:,-1].tail()

from sklearn.model_selection import train_test_split

data_train, data_test, label_train, label_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], test_size=0.3, random_state=0)

RFModel_SpamFilter = RandomForestClassifier(n_estimators=99, random_state=1).fit(data_train, label_train)

predicted_labels = RFModel_SpamFilter.predict(data_test)

metrics.confusion_matrix(label_test, predicted_labels)

# 1 - spam; 0 - non-spam
label_test [label_test == 1].count(), label_test [label_test == 0].count()

RFModel_SpamFilter.score (data_train, label_train)

RFModel_SpamFilter.score(data_test, label_test)

