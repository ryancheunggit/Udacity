import numpy
import matplotlib.pyplot as plt

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()



from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(ages_train, net_worths_train)

### get Katie's net worth (she's 27)
### sklearn predictions are returned in an array,
### so you'll want to do something like net_worth = predict([27])[0]
### (not exact syntax, the point is that [0] at the end)
km_net_worth = reg.predict([27])[0]

### get the slope
### again, you'll get a 2-D array, so stick the [0][0] at the end
slope = reg.coef_[0][0]

### get the intercept
### here you get a 1-D array, so stick [0] on the end to access
### the info we want
intercept = reg.intercept_[0]

### get the score on test data
test_score = reg.score(ages_test, net_worths_test)

### get the score on the training data
training_score = reg.score(ages_train, net_worths_train)


def submitFit():
    return {"networth":km_net_worth,
            "slope":slope,
            "intercept":intercept,
            "stats on test":test_score,
            "stats on training": training_score}