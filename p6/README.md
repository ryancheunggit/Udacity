
# List of files in the submission:
+ train.csv: the original data file
+ data.csv: the processed data file for the first version of visualization
+ pdata.csv: the processed data file for the second version of visualization
+ index.html: the first version of the visualization
+ version2.html: the second/final version of the visualization
+ dataProcess.R: the R code for processing the data file

# Summary:
+ Females passengers and young males(under age 15) from middle and upper class have high rate surviving the disaster.
+ The overall survivor rate for female passengers is higher than male passengers.</li>

# Design:
+ Each rectangle in the graph represents a passenger on Titanic, color red means that the passenger survived the disaster and the color blue indicates the opposite.
+ There can be multiple people with the same age, gender, and class values, so I set the opacity of these rectangles to be 20%. The places on the graph where you can see solid red shows that those passengers have a higher chance of surviving, whereas solid blue indicates danger.
+ You can move mouse over the rectangles to see deatiled summary information on surviving rates.

# Feedbacks:
+ Person1: The color yellow is not very clear when opacity is low. The side and spacing can be adjusted a little bit. Should give some instruction on how to read the graph.
+ Person2: The upper class(class = 1) should be on top, and the lower class (class = 3) should be on the bottom. This is more nature for readers.
+ Person3: The mouse over tool tip shows information about a perticular person, wheras there could be multiple person overlay on the same spot. Better show some aggregated information instead.

# Changes made based on feedbacks:
+ Change color of rectangle for died passengers to red.
+ Made the size of rectangle as well as the size of the visualization smaller.
+ Calculated summary information and are now shown as tool tip.
+ Adjusted the order of classes shown in the visualization. 
+ Added introduction on how to read the visualization.

# Resources:
+ http://bl.ocks.org/Caged/6476579: example for adding tool tip
+ https://github.com/mbostock/d3/wiki: d3 documentation
+ https://www.kaggle.com/c/titanic: the source of dataset used
