import pandas
import pandasql

def aggregate_query(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.

    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Write a query that will select from the aadhaar_data table how many men and how
    # many women over the age of 50 have had aadhaar generated for them in each district
    #
    # Note that in this quiz, the SQL query keywords are case sensitive.
    # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
    #

    # The possible columns to select from aadhaar data are:
    #     1) registrar
    #     2) enrolment_agency
    #     3) state
    #     4) district
    #     5) sub_district
    #     6) pin_code
    #     7) gender
    #     8) age
    #     9) aadhaar_generated
    #     10) enrolment_rejected
    #     11) residents_providing_email,
    #     12) residents_providing_mobile_number
    #
    # You can download a copy of the aadhaar data that we are passing
    # into this exercise below:
    # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    q = """
    select gender, district, sum(aadhaar_generated)
    from aadhaar_data
    where age > 50
    group by gender,district;
        """

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

print aggregate_query('aadhaar_data.csv')
