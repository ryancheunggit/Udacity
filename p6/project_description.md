# List of files in the submission:
1. README.md(this file): a description of the submission. 
2. train.csv: the original data file.
3. data.csv: the processed data file for the first version of visualization.
4. pdata.csv: the processed data file for the second version of visualization.
5. sdata.csv: the processed data file for the second visualization added in version 3.
6. index.html: the first version of the visualization.
7. version2.html: the second version of the visualization.
8. version3.html: the thrid version of the visualization.
9. dataProcess.R: the R code for processing the data file.
10. css folder: contain css file for the project.
11. js folder: contain javascript files for the project.

# Summary of findings:
+ Females passengers and young males(under age 15) from middle and upper class have high rate surviving the disaster.
+ The overall survivor rate for female passengers is higher than male passengers.</li>

# Design:
+ I created the visualizations with two questions I wish to answer. 
	1. The first question is: were older people, women as well as children been provied with help so that they have higher chance of surviving. 
	2. The second question is: were social and economical class affect the chance of surviving the diaster. 
+ In order to answer thest questions, I would incorporate all these dimensions into the visualizations. 
+ I designed this visualization presenting two different visualizations in the same page. 
	1. The first visualization is a set of two scatter plots. A scatter plot on top showing the male passengers in the data set, and the scatter plot on the bottom showing the female passengers in the dataset. This visualization would allow view to find interesting stories on their own.
		- In each of the scatter plots, the x axis is age whearas the y axis is class.  
		- Each rectangle in the scatter plots represents a passenger, color red means that the passenger survived the disaster and the color blue indicates the opposite.		
		- I decided to use red for Survived and blue for Died in the first visualization, simply because they are the primary colors from the rgb color model. I thought that they are quite different such that no person would misread the color coding. If I used red and orange, viewer would not be very hard in order to distinguish them. 
		- There can be multiple people with the same age, gender, and class values, so I set the opacity of these rectangles to be 20%. The places on the graph where you can see solid red shows that those passengers not only have a higher chance of surviving but also there were many passengers like them.
		- I added tooltip so that viewer can move mouse over the rectangles to see deatiled summary information on surviving rates.
	2. The second visualization is a grouped bar charts allow view to see the difference between survive rate between male and female passengers across different classes. 
		- There are two groups of bar charts, on the left side are the bar charts representing the survive rates for female passengers of different classes, and on the right side are the bar charts representing the survive rates for male passengers of different classes.
		- The bars are color coded as well, these colors are picked so that they are similar to each other but still the differences are enough for viewers to distinguish one from another. 

# Feedbacks:
+ Person1 a CS Professor : 
	- What you notice in the visualization?
		1. The color yellow is not very clear when opacity is low. 
		2. The side and spacing can be adjusted a little bit. 
		3. Should give some instruction on how to read the graph.
	- What do you think is the main takeaway from this visualization?
		1. Females and Children have higher rate of surviving. 
		2. I can use this plot to show student how to make a decision tree model.

+ Person2 my mother: 
	- What you notice in the visualization?
		1. The upper class(class = 1) should be on top, and the lower class (class = 3) should be on the bottom. This is more nature for readers.
	- What questions do you have about the data?
		1. How many passengers are there on Titanic?
		2. Which rectangle is Jack, and which one is Rose?
	- What do you think is the main takeaway from this visualization?
		1. Getting higher in social/economical class is always better. "You should try harder to earn more money and network with higher class people" ..................

+ Person3 my wife: 
	- What you notice in the visualization?
		1. The mouse over tool tip shows information about a perticular person, wheras there could be multiple person overlay on the same spot. Better show some aggregated information instead.
	- What questions do you have about the data?
		1. Does the data tell us who is married to who? What is the rate that two married people all survived from it?
		2. Can we know how many family members a passenger is traveling with and whould that affect the survive rate? More family members more help or more family members more diffult? 

# Changes made based on feedbacks:
+ Change color of rectangle for died passengers to red.
+ Made the size of rectangle as well as the size of the visualization smaller.
+ Calculated summary information and are now shown as tool tip.
+ Adjusted the order of classes shown in the visualization. 
+ Added introduction on how to read the visualization.

# Changes made after first review from Udacity
+ Added a second visualiztion.
+ Added more description on design and feedbacks.
+ Reorganized the code, used external files for javascript and css. 

# Resources:
+ http://bl.ocks.org/Caged/6476579: example for adding tool tip
+ https://github.com/mbostock/d3/wiki: d3 documentation
+ https://www.kaggle.com/c/titanic: the source of dataset used
+ http://bl.ocks.org/mbostock/3887051: example for a grouped bar chart