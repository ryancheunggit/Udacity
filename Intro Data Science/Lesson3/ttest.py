import scipy.stats
list_1 = [1,2,3,4,5,6,7]
list_2 = [2,3,4,5,6,6,8]
t, p = scipy.stats.ttest_ind(list_1,list_2,equal_var = False)
print "p value is:",p
print "t value is:",t
