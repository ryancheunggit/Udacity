#!/usr/bin/python
from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#t0 = time()
#knnClf = KNeighborsClassifier()
#knnClf.fit(features_train, labels_train)
#print "default knn training time:", round(time()-t0, 3), "s"

t0 = time()
adaBoostClf = AdaBoostClassifier(n_estimators=30,learning_rate=0.4)
adaBoostClf.fit(features_train, labels_train)
print "default adaBoost training time:", round(time()-t0, 3), "s"

#t0 = time()
#rfClf = RandomForestClassifier()
#rfClf.fit(features_train, labels_train)
#print "default randomForest training time:", round(time()-t0, 3), "s"

#knnPred = knnClf.predict(features_test)
#knnacc = accuracy_score(knnPred, labels_test)

adaBoostPred = adaBoostClf.predict(features_test)
adaBoostacc = accuracy_score(adaBoostPred, labels_test)

#rfPred = rfClf.predict(features_test)
#rfacc = accuracy_score(rfPred, labels_test)

# print "default knn accuracy:", knnacc
print "default adaBoost accuracy:", adaBoostacc
# print "default rf accuracy:", rfacc

8

try:
    prettyPicture(adaBoostClf, features_test, labels_test)
except NameError:
	print "unable to produce boundary"
    pass
