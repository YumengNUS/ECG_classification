# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:51:06 2019

@author: Yumeng
"""



import wfdb
import matplotlib.pyplot as plt
import numpy as np
import pywt 
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

from read_ecg import read_ecg 
from plot_ecg import plot_ecg 
from extract_data import extract_data_from_train_file,extract_data_from_test_file
from extract_feature import simple_f,wavelets_f

# read all the training data and put them in one array
x_total=[]
y_total=[]
for i in range(1,7):
    path="C:\\E\\Jobs\\Biofourmis\\ECG\\database\\train\\a"+str(i)
    x ,y = extract_data_from_train_file(path)
    x_total.extend(x)
    y_total.extend(y)

x_total=np.array(x_total)
y_total=np.array(y_total)


#feature extraction: simple feature and wavelets feature
n = len(x_total[:,1])
trainingdata1 = simple_f(x_total,n)
trainingdata2 = wavelets_f(x_total)
x_feature = np.hstack((trainingdata1,trainingdata2))




#shuffle data
x_feature,y_total=shuffle(x_feature,y_total)
idx=int(len(x_feature)*0.7)
x_train=x_feature[:idx]
x_valid=x_feature[idx:]
y_train=y_total[:idx]
y_valid=y_total[idx:]


# cross-validation for choosing model (logistic regression or svm)
clf_lr = LogisticRegression(solver='liblinear',class_weight='balanced',max_iter=1000)
clf_rbf = SVC(kernel='rbf',class_weight='balanced')
scores_lr = cross_val_score(clf_lr, x_feature, y_total, cv=10, scoring='accuracy')
scores_rbf = cross_val_score(clf_rbf, x_feature, y_total, cv=10, scoring='accuracy')
print(scores_lr.mean(),scores_rbf.mean())

#machine learning model(SVM)
clf_rbf.fit(x_train,y_train)
pred_valid=clf_rbf.predict(x_valid)
print (classification_report(y_valid, pred_valid))
fpr, tpr, thresholds = metrics.roc_curve(y_valid, pred_valid)
print(metrics.auc(fpr, tpr))

#3. The assigned 'V' beat info shall be exported to WFDB format (*.test),
# and sent back to Biofourmis.
for index in range(1,3):
    path="C:\\E\\Jobs\\Biofourmis\\ECG\\database\\test\\b"+str(index)
    x_test ,location = extract_data_from_test_file(path)
    n = len(x_test)
    x_test = np.array(x_test)
    testingdata1 = simple_f(x_test,n)
    testingdata2 = wavelets_f(x_test)
    x_feature_test = np.hstack((testingdata1,testingdata2))
    predicted_labels=clf_rbf.predict(x_feature_test)
    ecg_sig, ecg_type, ecg_peak = read_ecg(path)
    for i in range(len(location)):
        if predicted_labels[i]==1:
            ecg_type[location[i]]="V"
    
    name="b"+str(index)
    wfdb.wrann(name, 'test', ecg_peak, ecg_type, write_dir='C:\\E\\Jobs\\Biofourmis\\ECG\\database\\test\\')









