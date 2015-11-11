#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# A smaller training set uncomment the following two lines to test
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
# clf = SVC(kernel="linear")
# clf = SVC(kernel ="rbf")
# clf = SVC(kernel = "rbf", C = 10) 
# clf = SVC(kernel = "rbf", C = 100) 
# clf = SVC(kernel = "rbf", C = 1000) 
clf = SVC(kernel = "rbf", C = 10000) 

clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

acc = accuracy_score(pred, labels_test)

print "The predcition accuracy is: ",acc


print "prediction for the 10th test case",pred[10]

print "prediction for the 26th test case",pred[26]

print "prediction for the 50th test case",pred[50]

s = 0
for p in pred:
	if p == 1:
		s += 1

print s