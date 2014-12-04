from pandas import DataFrame, Series
import numpy as np


def create_dataframe():
    '''
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the table of 2014 Sochi winter olympics medal counts.

    The columns for this dataframe should be called
    'country_name', 'gold', 'silver', and 'bronze'.

    There is no need to  specify row indexes for this dataframe
    (in this case, the rows will automatically be assigned numbered indexes).

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medal_counts_df = DataFrame({"country_name":countries,
                                         "gold":gold,
                                         "silver":silver,
                                         "bronze":bronze})

    return olympic_medal_counts_df


df = create_dataframe()

print df

# print a column of the dataframe
print df['gold']

# print a row of the dataframe
print df.loc[0]


print df.loc[:,['gold','silver','bronze']].apply(np.mean)

print df['gold'].map(lambda x: x >5)

print df[['gold','silver']]

print df.loc[:,['gold','silver','bronze']].applymap(lambda x: x >=1)
