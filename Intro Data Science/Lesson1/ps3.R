
library(rpart)
library(rpart.plot)
df <- read.csv("titanic_data.csv")

model  <- rpart(Survived~Pclass+Sex+Age+SibSp+Parch+Fare+Embarked, data = df, method = "class", maxdepth = 3)
lmpred <- predict(model, newdata = df, type = "class")
t = table(lmpred, df$Survived)
(t[1]+t[4])/sum(t)



prp(model)
print(model)


model  <- rpart(Survived~Pclass+Sex, data = df, method = "class")
table(df$Pclass)
