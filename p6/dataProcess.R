# Author: Ren Zhang
# email:zhang_ren@bentley.edu
# code for processing data files used for Udacity data visualization project 

# library
library(dplyr)

# set up working directory
setwd("D:/GithubRepos/Udacity/p6")

# read in the original training data got from Kaggle website
data <- read.csv("train.csv")

# remove observations with na fields from dataset
data <- na.omit(data)

# write out file for visuailzation (used for the first version of Viz)
write.csv(data, "data.csv", row.names = F)

# updated Jan 11th
# summary groups of people with same gender, class and age
# the summary information will be used for providing better tooltip info
by_gender_class_age <- group_by(data, Sex, Pclass, Age)

sumData <- summarise(by_gender_class_age, 
          numTotal = n(),
          numSurvived = sum(Survived),
          numDied = numTotal - numSurvived,
          surviveRate = round(numSurvived/numTotal,2) * 100)

pdata <- inner_join(data, sumData)

# write out data file for the improved data visualization
write.csv(pdata, "pdata.csv", row.names = F)

# updated Jan 24th
# process data for bar chart
by_gender_class <- group_by(data, Sex, Pclass)
sumData <- summarise(by_gender_class, 
                     surviveRate = round(sum(Survived)/n(),2) * 100)
meltedSumData <- melt(sumData, id.vars = c("Sex", "Pclass"))
sdata <- dcast(meltedSumData, Sex~Pclass)
names(sdata)[2:4] <- c("Upper", "Middle", "Lower")

# write out file
write.csv(sdata, "sdata.csv", row.names = F)