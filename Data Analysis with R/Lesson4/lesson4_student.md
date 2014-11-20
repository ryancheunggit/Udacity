Lesson 4
========================================================
read in data

```
## Warning: New theme missing the following elements: legend.box,
## panel.margin.x, panel.margin.y
```

### Scatterplots and Perceived Audience Size
qplot

```r
qplot(x = age, y = friend_count, data = pf)
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-2-1.png) 

equalvent ggplot

```r
ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_point()
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3-1.png) 

limit the x axis

```r
ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_point() +
  xlim(13,90)
```

```
## Warning: Removed 4906 rows containing missing values (geom_point).
```

![plot of chunk unnamed-chunk-4](figure/unnamed-chunk-4-1.png) 

add transparent and jitter to look through the overlapping points
### Overplotting

```r
ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_jitter(alpha = 1/20) +
  xlim(13,90)
```

```
## Warning: Removed 5207 rows containing missing values (geom_point).
```

![plot of chunk Overplotting](figure/Overplotting-1.png) 

#### What do you notice in the plot?
Response: most young user have friends less than 1000, not significantly bigger than older user.

### Coord_trans()

```r
ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_point(alpha = 1/20, position = position_jitter(h = 0)) +
  xlim(13,90) +
  coord_trans(y = "sqrt")
```

```
## Warning: Removed 5183 rows containing missing values (geom_point).
```

![plot of chunk Coord_trans()](figure/Coord_trans()-1.png) 


```r
ggplot(aes(x = age, y = friendships_initiated), data = pf) + 
  geom_point(alpha = 1/20, position = position_jitter(h=0))+
  xlim(13,90) + 
  coord_trans(y = "sqrt")
```

```
## Warning: Removed 5191 rows containing missing values (geom_point).
```

![plot of chunk unnamed-chunk-5](figure/unnamed-chunk-5-1.png) 

### Conditional Means


```r
#install.packages('dplyr')
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
## 
## The following object is masked from 'package:stats':
## 
##     filter
## 
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
age_groups <- group_by(pf, age)
pf.fc_by_age <- summarise(age_groups, 
          friend_count_mean = mean(friend_count),
          friend_count_median = median(friend_count),
          n = n())
pf.fc_by_age <- arrange(pf.fc_by_age,age)
```

equal to

```r
pf.fc_by_age <- pf %>%
  group_by(age) %>%
  summarise(friend_count_mean = mean(friend_count),
            friend_count_median = median(friend_count),
            n = n()) %>%
  arrange(age)

pf.fc_by_age
```

```
## Source: local data frame [101 x 4]
## 
##    age friend_count_mean friend_count_median    n
## 1   13          164.7500                74.0  484
## 2   14          251.3901               132.0 1925
## 3   15          347.6921               161.0 2618
## 4   16          351.9371               171.5 3086
## 5   17          350.3006               156.0 3283
## 6   18          331.1663               162.0 5196
## 7   19          333.6921               157.0 4391
## 8   20          283.4991               135.0 3769
## 9   21          235.9412               121.0 3671
## 10  22          211.3948               106.0 3032
## .. ...               ...                 ...  ...
```

# Plot mean friend count vs. age using a line graph.
# Be sure you use the correct variable names
# and the correct data frame. You should be working
# with the new data frame created from the dplyr
# functions. The data frame is called 'pf.fc_by_age'.

# Use geom_line() rather than geom_point to create
# the plot. You can look up the documentation for
# geom_line() to see what it does.

Create your plot!


```r
ggplot(aes(x = age, y = friend_count_mean), data = pf.fc_by_age)+
  geom_line()
```

![plot of chunk Conditional Means Plot](figure/Conditional Means Plot-1.png) 

### Overlaying Summaries with Raw Data

```r
ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_point(alpha = 1/20,
             position = position_jitter(h = 0),
             color = "orange") +
  xlim(13,90) +
  coord_trans(y = "sqrt") +
  geom_line(stat = "summary", fun.y = mean) +
  geom_line(stat = "summary", fun.y = quantile, probs = .1,
            linetype = 2, color = 'blue') + 
  geom_line(stat = "summary", fun.y = quantile, probs = .9,
            linetype = 2, color = 'red') +
  geom_line(stat = "summary", fun.y = quantile, probs = .5,
            linetype = 2, color = 'green')
```

```
## Warning: Removed 4906 rows containing missing values (stat_summary).
```

```
## Warning: Removed 4906 rows containing missing values (stat_summary).
```

```
## Warning: Removed 4906 rows containing missing values (stat_summary).
```

```
## Warning: Removed 4906 rows containing missing values (stat_summary).
```

```
## Warning: Removed 5172 rows containing missing values (geom_point).
```

![plot of chunk Overlaying Summaries with Raw Data](figure/Overlaying Summaries with Raw Data-1.png) 

Better plot

```r
ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_point(alpha = 1/20,
             position = position_jitter(h = 0),
             color = "orange") +
  coord_cartesian(xlim = c(13,70), ylim = c(0,1000)) +
  geom_line(stat = "summary", fun.y = mean) +
  geom_line(stat = "summary", fun.y = quantile, probs = .1,
            linetype = 2, color = 'blue') + 
  geom_line(stat = "summary", fun.y = quantile, probs = .9,
            linetype = 2, color = 'red') +
  geom_line(stat = "summary", fun.y = quantile, probs = .5,
            linetype = 2, color = 'green')
```

![plot of chunk unnamed-chunk-7](figure/unnamed-chunk-7-1.png) 

### Correlation

```r
names(cor.test(pf$friend_count, pf$age))
```

```
## [1] "statistic"   "parameter"   "p.value"     "estimate"    "null.value" 
## [6] "alternative" "method"      "data.name"   "conf.int"
```

```r
round(cor.test(pf$friend_count, pf$age, meathod = "pearson")$estimate,3)
```

```
##    cor 
## -0.027
```

equal

```r
with(pf, cor.test(age, friend_count,method = "pearson"))
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  age and friend_count
## t = -8.6268, df = 99001, p-value < 2.2e-16
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.03363072 -0.02118189
## sample estimates:
##         cor 
## -0.02740737
```

### Correlation on Subsets

```r
with(subset(pf, pf$age <= 70) , cor.test(age, friend_count))
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  age and friend_count
## t = -52.5923, df = 91029, p-value < 2.2e-16
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.1780220 -0.1654129
## sample estimates:
##        cor 
## -0.1717245
```

### Correlation Methods

```r
with(subset(pf, pf$age <= 70), cor.test(age, friend_count,method = "spearman"))
```

```
## Warning in cor.test.default(age, friend_count, method = "spearman"):
## Cannot compute exact p-value with ties
```

```
## 
## 	Spearman's rank correlation rho
## 
## data:  age and friend_count
## S = 1.5782e+14, p-value < 2.2e-16
## alternative hypothesis: true rho is not equal to 0
## sample estimates:
##        rho 
## -0.2552934
```

## Create Scatterplots
# Create a scatterplot of likes_received (y)
# vs. www_likes_received (x). Use any of the
# techniques that you've learned so far to
# modify the plot.

```r
ggplot(aes(x = www_likes_received,  y = likes_received), data = pf) +
  geom_point()
```

![plot of chunk unnamed-chunk-10](figure/unnamed-chunk-10-1.png) 

### Strong Correlations

```r
ggplot(aes(x = www_likes_received,  y = likes_received), data = pf) +
  geom_point(alpha = 1/4) +
  xlim(0, quantile(pf$www_likes_received, 0.95)) +
  ylim(0, quantile(pf$likes_received, 0.95))+
  geom_smooth(method = "lm", color = 'red')
```

```
## Warning: Removed 6075 rows containing missing values (stat_smooth).
```

```
## Warning: Removed 6075 rows containing missing values (geom_point).
```

![plot of chunk Strong Correlations](figure/Strong Correlations-1.png) 

What's the correlation betwen the two variables? Include the top 5% of values for the variable in the calculation and round to 3 decimal places.


```r
round(with(pf, cor.test(www_likes_received, likes_received))$estimate,3)
```

```
##   cor 
## 0.948
```

### More Caution with Correlation

```r
#install.packages('alr3')
library(alr3)
```

```
## Loading required package: car
```

```r
data(Mitchell)
```


```r
ggplot(aes(x = Month, y = Temp), data = Mitchell) +
  geom_point()
```

![plot of chunk Temp vs Month](figure/Temp vs Month-1.png) 

### Noisy Scatterplots
a. Take a guess for the correlation coefficient for the scatterplot.

0

b. What is the actual correlation of the two variables?
(Round to the thousandths place)


```r
cor(Mitchell$Month, Mitchell$Temp)
```

```
## [1] 0.05747063
```

### Making Sense of Data

```r
ggplot(aes(x = Month, y = Temp), data = Mitchell) +
  geom_point()+
  scale_x_discrete(breaks = seq(0,203,12))
```

![plot of chunk Making Sense of Data](figure/Making Sense of Data-1.png) 

### A New Perspective

```r
ggplot(aes(x = Month, y = Temp), data = Mitchell) +
  geom_point()+
  scale_x_discrete(breaks = seq(0,203,12))
```

![plot of chunk New Perspective](figure/New Perspective-1.png) 

### Understanding Noise: Age to Age Months

```r
ggplot(aes(x = age, y = friend_count_mean), data = pf.fc_by_age) +
  geom_line()
```

![plot of chunk Age to Age Months](figure/Age to Age Months-1.png) 

```r
head(pf.fc_by_age)
```

```
## Source: local data frame [6 x 4]
## 
##   age friend_count_mean friend_count_median    n
## 1  13          164.7500                74.0  484
## 2  14          251.3901               132.0 1925
## 3  15          347.6921               161.0 2618
## 4  16          351.9371               171.5 3086
## 5  17          350.3006               156.0 3283
## 6  18          331.1663               162.0 5196
```

```r
pf.fc_by_age[17:19,]
```

```
## Source: local data frame [3 x 4]
## 
##   age friend_count_mean friend_count_median    n
## 1  29          120.8182                66.0 1936
## 2  30          115.2080                67.5 1716
## 3  31          118.4599                63.0 1694
```

### Age with Months Means


```r
pf$age_with_months <- pf$age + (12 - pf$dob_month) / 12
```

Programming Assignment

```r
age_with_months_groups <- group_by(pf, age_with_months)
pf.fc_by_age_months <- summarise(age_with_months_groups,
                                 friend_count_mean = mean(friend_count),
                                 friend_count_median = median(friend_count),
                                 n = n())
arrange(pf.fc_by_age_months, age_with_months)
```

```
## Source: local data frame [1,194 x 4]
## 
##    age_with_months friend_count_mean friend_count_median   n
## 1         13.16667          46.33333                30.5   6
## 2         13.25000         115.07143                23.5  14
## 3         13.33333         136.20000                44.0  25
## 4         13.41667         164.24242                72.0  33
## 5         13.50000         131.17778                66.0  45
## 6         13.58333         156.81481                64.0  54
## 7         13.66667         130.06522                75.5  46
## 8         13.75000         205.82609               122.0  69
## 9         13.83333         215.67742               111.0  62
## 10        13.91667         162.28462                71.0 130
## ..             ...               ...                 ... ...
```

### Noise in Conditional Means


```r
ggplot(aes(x = age_with_months, y = friend_count_mean), 
       data = subset(pf.fc_by_age_months, pf.fc_by_age_months$age_with_months <= 71)) +
  geom_line()
```

![plot of chunk Noise in Conditional Means](figure/Noise in Conditional Means-1.png) 

### Smoothing Conditional Means

```r
q1 <- ggplot(aes(x = age, y = friend_count_mean), 
            data = subset(pf.fc_by_age, pf.fc_by_age$age <= 71)) +
              geom_line() +
  geom_smooth()

q2 <- ggplot(aes(x = age_with_months, y = friend_count_mean), 
       data = subset(pf.fc_by_age_months, pf.fc_by_age_months$age_with_months <= 71)) +
  geom_line() + 
  geom_smooth()

q3 <- ggplot(aes(x = round(age/5)*5, y = friend_count),
             data = subset(pf, pf$age <= 71)) +
  geom_line(stat = 'summary', fun.y = mean)

library(gridExtra)
```

```
## Loading required package: grid
```

```r
grid.arrange(q1,q2,q3,ncol = 1)
```

```
## geom_smooth: method="auto" and size of largest group is <1000, so using loess. Use 'method = x' to change the smoothing method.
## geom_smooth: method="auto" and size of largest group is <1000, so using loess. Use 'method = x' to change the smoothing method.
```

![plot of chunk unnamed-chunk-11](figure/unnamed-chunk-11-1.png) 

Click **KnitHTML** to see all of your hard work and to have an html
page of this lesson, your answers, and your notes!

