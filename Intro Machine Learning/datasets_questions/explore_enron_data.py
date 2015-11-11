#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import os 

os.chdir("d:\GithubRepos\Udacity\Intro Machine Learning\datasets_questions")

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "the number of people in the dataset is: ",len(enron_data)

print "the number of features is: ",len(enron_data.values()[1])

print "the number of person of interset is: ", sum([1 for i in enron_data.values() if i['poi'] == True])

print "the total value of the stock belonging to James Prentice is: ", enron_data['PRENTICE JAMES']['total_stock_value']

for i in enron_data.keys():
	if i.startswith('C') or i.startswith('W'):
		print i

print "the number of email messages from Wesley Colwell to persons of interest is: ",enron_data['COLWELL WESLEY']['from_this_person_to_poi']

for i in enron_data.keys():
	if i.startswith('J') or i.startswith('S'):
		print i

print "the value of stock options exercised by Jeffrey Skilling is: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "the number of folks in this dataset have a quantified salary is: ", sum([1 for i in enron_data.values() if i['salary'] != 'NaN' ])

print "the number of folks in this dataset have a known email address is: ", sum([1 for i in enron_data.values() if i['email_address'] != 'NaN' ])

print "the number of people in the E+F dataset (as it currently exists) have 'NaN' for their total payments is: ",sum([1 for i in enron_data.values() if i['total_payments'] == 'NaN' ])

print "the percentage of people in the dataset as a whole is: ", 100*21.0/146
print "the number of POIs in the E+F dataset have 'NaN' for their total payment is: ", sum([1 for i in enron_data.values() if (i['total_payments'] == 'NaN' and i['poi']==True) ])
print "the percentage of POI’s as a whole is: ",0/18*100