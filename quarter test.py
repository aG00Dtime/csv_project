#  <--- code STARTS here --->
# import libs needed

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
# <----Csv file handling starts here---->
# read the csv file
csv_file = pd.read_csv(
    "Annual_Registration_Motor_Vehicles_2000_2018.csv", skiprows=[0])
# replace spaces with underscores in the header
csv_file.columns = [col.replace(
    " ",  "_") for col in csv_file.columns]

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
# the name of the dataframe is vehicle_registration_df - only select the 19 rows we used
vehicle_registration_df_quarterly_data = csv_file.iloc[23:53]

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
# convert datatypes to  ints except the year column
vehicle_registration_df_quarterly_data.loc[:,
                                           vehicle_registration_df_quarterly_data.columns != 'Period'].astype(float)
# thousands seperator for outputs,eg. 5,000 or 20,000 etc
pd.options.display.float_format = '{:,.0f}'.format
# <----Csv file handling ends here---->
# print(vehicle_registration_df_quarterly_data.fillna(''))
print(tabulate(vehicle_registration_df_quarterly_data,
               headers=vehicle_registration_df_quarterly_data.columns, showindex="never", floatfmt=",.2f", tablefmt='pretty'))
