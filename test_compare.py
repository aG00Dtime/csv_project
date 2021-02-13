# <--- code STARTS here --->

# import libs needed

import pandas as pd
import matplotlib.pyplot as plt

# <----Csv file handling starts here---->
# read the csv file
csv_file = pd.read_csv(
    "Annual_Registration_Motor_Vehicles_2000_2018.csv", skiprows=[0])

# only select the rows we want to use
vehicle_registration_df = csv_file.iloc[:19]

# disables the warming when we change the data from str to ints
pd.options.mode.chained_assignment = None

# converts the values in the df to  int
for row in vehicle_registration_df:
    vehicle_registration_df[row] = vehicle_registration_df[row].astype(int)
    # print(str(vehicle_registration_df[row]))

# make the year column a str so it doesn't break the  year filter and graphs
vehicle_registration_df.Period = vehicle_registration_df.Period.astype(str)

# replace spaces in header names with underscores
vehicle_registration_df.columns = [col.replace(
    " ",  "_") for col in vehicle_registration_df.columns]
# <----Csv file handling ends here---->

print(vehicle_registration_df)


def yeartoyear():
    df = vehicle_registration_df

    year1_ask = '2005'
    year2_ask = '2006'

    year1 = df[df.Period == year1_ask
               ]
    year2 = df[df.Period == year2_ask
               ]
    joint_years = [year1, year2]
    joint_years = pd.concat(joint_years)
