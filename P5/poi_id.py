#!/usr/bin/python

### Part 0 Setup and import library 
import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.cross_validation import train_test_split, StratifiedShuffleSplit
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import recall_score, accuracy_score, precision_score
from sklearn.preprocessing import MinMaxScaler
from tester import test_classifier
import pandas as pd
import numpy as np
from time import time
from matplotlib import pyplot as plt

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary' , 'deferral_payments', 'total_payments', 'loan_advances',
                 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 
                 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 
                 'restricted_stock', 'director_fees', 'to_messages', 'from_poi_to_this_person', 
                 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']

print "number of features to start with: ",len(features_list) - 1

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
print "number of data points in the dataset: ", len(data_dict)

print "print out the person names in the dataset: "
s = []
for person in data_dict.keys():
    s.append(person)
    if len(s) == 4:
        print '{:<30}{:<30}{:<30}{:<30}'.format(s[0],s[1],s[2],s[3])
        s = []
print '{:<30}{:<30}'.format(s[0],s[1])

print "'Total' is obviously an outlier so we will remove it from the dataset"

npoi = 0
for p in data_dict.values():
    if p['poi']:
        npoi += 1
print "number of person of interest is: ", npoi
print "number of person who is not of interset is: ", len(data_dict) - npoi


print "print out the number of missing values in each feature: "
NaNInFeatures = [0 for i in range(len(features_list))]
for i, person in enumerate(data_dict.values()):
    for j, feature in enumerate(features_list):
        if person[feature] == 'NaN':
            NaNInFeatures[j] += 1

for i, feature in enumerate(features_list):
    print feature, NaNInFeatures[i]

print "print out some values of the observation 'TOTAL'"
for name, person in data_dict.iteritems():
	if name == 'TOTAL':
		print person

salary  = []
for name, person in data_dict.iteritems():
    if float(person['salary']) > 0:
        salary.append(float(person['salary']))
print "the sum of salary of all other persons is: ",np.sum(salary)/2 

## Remove the outlier
data_dict.pop('TOTAL')


print "number of data points in the dataset after remove 'TOTAl' is : ", len(data_dict)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict


print "we create two new features here 'to_poi_message_ratio' and 'from_poi_message_ratio' "
for person in my_dataset.values():
    person['to_poi_message_ratio'] = 0
    person['from_poi_message_ratio'] = 0
    if float(person['from_messages']) > 0:
        person['to_poi_message_ratio'] = float(person['from_this_person_to_poi'])/float(person['from_messages'])
    if float(person['to_messages']) > 0:
        person['from_poi_message_ratio'] = float(person['from_poi_to_this_person'])/float(person['to_messages'])
    
features_list.extend(['to_poi_message_ratio', 'from_poi_message_ratio'])

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

## Try to use stratifieldshufflesplit to find the best subset of features to use
print "start selecting feautres: "
scv = StratifiedShuffleSplit(labels, 1000, random_state = 42)
RF_acc = []
RF_precision = []
RF_recall = []
ADA_acc = []	
ADA_precision = []
ADA_recall = []

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html


def cvClassifier(clf, features, labels, cv):
	### function to help train and evaluate classifiers using crossvalidation
    true_negatives = 0
    false_negatives = 0
    true_positives = 0
    false_positives = 0
    for train_idx, test_idx in cv: 
        features_train = []
        features_test  = []
        labels_train   = []
        labels_test    = []
        for ii in train_idx:
            features_train.append( features[ii] )
            labels_train.append( labels[ii] )
        for jj in test_idx:
            features_test.append( features[jj] )
            labels_test.append( labels[jj] )
        clf.fit(features_train, labels_train)
        predictions = clf.predict(features_test)
        for prediction, truth in zip(predictions, labels_test):
            if prediction == 0 and truth == 0:
                true_negatives += 1
            elif prediction == 0 and truth == 1:
                false_negatives += 1
            elif prediction == 1 and truth == 0:
                false_positives += 1
            elif prediction == 1 and truth == 1:
                true_positives += 1
    total_predictions = true_negatives + false_negatives + false_positives + true_positives
    accuracy = round(1.0*(true_positives + true_negatives)/total_predictions,2)
    precision = round(1.0*true_positives/(true_positives+false_positives),2)
    recall = round(1.0*true_positives/(true_positives+false_negatives),2)
    return accuracy, precision, recall

print "we train both a randomforest and an adaboost model for each of the best k features "
print "warning this is slow..."
for i in range(len(features[0])):
    t0 = time()
    selector = SelectKBest(f_classif, k = i+1)
    selector.fit(features, labels)
    reduced_features = selector.fit_transform(features, labels)
    cutoff = np.sort(selector.scores_)[::-1][i]
    selected_features_list = [f for j, f in enumerate(features_list[1:]) if selector.scores_[j] >= cutoff]
    selected_features_list = ['poi'] + selected_features_list
    RF = RandomForestClassifier(random_state=1126)
    adaBoost = AdaBoostClassifier(random_state=1126)
    acc, precision, recall = cvClassifier(RF, reduced_features, labels, scv)
    RF_acc.append(acc)
    RF_precision.append(precision)
    RF_recall.append(recall)
    acc, precision, recall = cvClassifier(adaBoost, reduced_features, labels, scv)
    ADA_acc.append(acc)
    ADA_precision.append(precision)
    ADA_recall.append(recall)
    print "fitting time for k = {0}: {1}".format(i+1, round(time()-t0, 3))
    print "RF accuracy: {0}  precision: {1}  recall: {2}".format(RF_acc[-1], RF_precision[-1], RF_recall[-1])
    print "ADA accuracy: {0}  precision: {1}  recall: {2}".format(ADA_acc[-1], ADA_precision[-1], ADA_recall[-1])




print "plotting the scores for each classifiers for different best k features used"
rfdf = pd.DataFrame({'RF_acc': RF_acc, 'RF_pre': RF_precision, 'RF_rec': RF_recall})
adadf = pd.DataFrame({'ADA_acc': ADA_acc, 'ADA_pre': ADA_precision, 'ADA_rec': ADA_recall})                   
rfdf.plot()
plt.show()
adadf.plot()
plt.show()

print "It appears that using random forest model will tend to have higher precision and lower recall."     
print "For adaboost model it tend to have higher recall but lower precision."       
print "And the accuracy for both classifiers are about the same."

selector = SelectKBest(f_classif, k = ADA_recall.index(max(ADA_recall))+1)
selector.fit(features, labels)
cutoff = np.sort(selector.scores_)[::-1][ADA_recall.index(max(ADA_recall))+1]
selected_features_list = [f for i, f in enumerate(features_list[1:]) if selector.scores_[i] > cutoff]
selected_features_list = ['poi'] + selected_features_list
selected_features = selector.fit_transform(features, labels)

print "number of features selected: ", len(selected_features_list)-1
print "and they are: "
for f in selected_features_list[1:]:
    print f

RF = RandomForestClassifier(random_state=1126)
RF.fit(selected_features, labels)
print "the feature importance for these selected features are: "
print RF.feature_importances_

print "the feature scores for these selected features from SelectKBest are: "
for f in selected_features_list[1:]:
	print f, "score is: ", selector.scores_[features_list[1:].index(f)]

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

## tuning the randomforest
t0 = time()
tuning_parameters = {'n_estimators': [20,50,100], 'min_samples_split': [1,2,4], 'max_features': [1,2,3]}
print("# Tuning hyper-parameters for recall")
RF = GridSearchCV(RandomForestClassifier(), tuning_parameters, cv=scv, scoring = 'recall')
RF.fit(selected_features, labels)
print("Best parameters are:")
print(RF.best_params_)
print "tunning time: {0}".format(round(time()-t0, 3))

Clf = RF.best_estimator_
print "measurements for tuned random forest classifier: "
test_classifier(Clf, my_dataset, selected_features_list, folds = 1000)


## tuning the adaboost
t0 = time()
tuned_parameters = {'n_estimators': [50,100,200], 'learning_rate': [0.4,0.6,1]}
print("# Tuning hyper-parameters for recall")
Adaboost = GridSearchCV(AdaBoostClassifier(), tuned_parameters, cv=scv, scoring = 'recall')
Adaboost.fit(selected_features, labels)
print("Best parameters are:")
print(Adaboost.best_params_)
print "tunning time: {0}".format(round(time()-t0, 3))

Clf = Adaboost.best_estimator_
print "measurements for tuned adaboost classifier: "
test_classifier(Clf, my_dataset, selected_features_list, folds = 1000)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

Clf = RF.best_estimator_
dump_classifier_and_data(Clf, my_dataset, selected_features_list)