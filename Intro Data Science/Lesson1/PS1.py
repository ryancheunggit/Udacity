import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.

    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted

    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data.

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic diaster.

    You prediction should be 78% accurate or higher.

    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.

    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survied or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0

    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''
    df = pandas.read_csv(file_path)
    predictions = {}

    for passenger_index, passenger in df.iterrows():
        if passenger['Sex'] == 'male':
            predictions[passenger['PassengerId']] = 0
        elif passenger['Sex'] == 'female':
            predictions[passenger['PassengerId']] = 1
    return predictions
