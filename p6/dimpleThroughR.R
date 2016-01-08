setwd("D:/GithubRepos/Udacity/p6")

library(dimple)

data <- read.csv("train.csv")

head(data)


dimple(data,
       xCategory="Survived",
       yMeasure="Age",
       series = "SibSp")
