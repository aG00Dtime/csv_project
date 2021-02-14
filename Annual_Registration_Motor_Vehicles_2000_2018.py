# need to install these libs to be able to run this
# https://matplotlib.org/stable/index.html
# https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
# https://pypi.org/project/tabulate/
# https://numpy.org/

# output data->done
# summaries-> done
# graphs--> done
#
#  <--- code STARTS here --->

# import libs needed

from numpy.lib.function_base import diff
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
vehicle_registration_df = csv_file.iloc[:19]


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
# convert datatypes to  ints except the year column
vehicle_registration_df.loc[:,
                            vehicle_registration_df.columns != 'Period'].astype(float)
# thousands seperator for outputs,eg. 5,000 or 20,000 etc
pd.options.display.float_format = '{:,.0f}'.format

# <----Csv file handling ends here---->


def summaries():
    '''SUMMARIES'''
    # https: // pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

    # print summaries
    print("\nAVERAGE VEHICLES (BY TYPE) REGISTERED PER YEAR FROM 2000 - 2018 (Sorted from Highest to Lowest)\n")
    print(vehicle_registration_df[['Private_Cars', 'Hire_Cars', 'Lorries', 'Buses',
                                   'Station_Wagons', 'Vans', 'Tractors', 'Trailers', 'Motorcycles', 'Other']].mean().sort_values(ascending=False).to_string())
    # converted to float because base values are ints
    print("\nTOTAL VEHICLES (BY TYPE) REGISTERED FROM 2000 - 2018 (Sorted from Highest to Lowest)\n ")
    print(vehicle_registration_df[['Private_Cars', 'Hire_Cars', 'Lorries', 'Buses',
                                   'Station_Wagons', 'Vans', 'Tractors', 'Trailers', 'Motorcycles', 'Other']].sum().sort_values(ascending=False).to_string())

    print("\nTOTAL VEHICLES REGISTERED FROM 2000 - 2018\n ")
    # converted to float because base values are ints
    print((vehicle_registration_df[['Total']].sum().to_string()))
    # need to do this


def graphs():
    '''graphs'''
    while True:
        print(
            "\nTo view a graphs that shows all registered vehicles during the period 2000 - 2018 Press [1]\nTo view a graph that compares the total vehicles registered per year during the period 2000 to 2018 Press [2]\nTo exit this menu press [3]")
        user_graph_choice = input("Choice : ")

        if int(user_graph_choice) == 1:
            # plot.bar plots everthing in the dataframe next to each other
            # vehicle_registration_df.plot(x='Period')

            # private cars
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Private_Cars)
            # lorries

            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Lorries)
            # vans

            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Vans)
            # hire cars
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Hire_Cars)
            # buses
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Buses)
            # Station Wagons
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Station_Wagons)
            # tractors
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Tractors)

            # trailers
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Trailers)
            # motorcycles
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Motorcycles)

            # other vehicles
            plt.plot((vehicle_registration_df.Period),
                     vehicle_registration_df.Other)

            # labels
            plt.xlabel("Years")
            plt.ylabel("Amount of Vehicles Registered")
            plt.legend(['Private cars', 'Lorries',
                        'Vans', 'Hire Cars', "Buses", 'Station Wagons', 'Tractors', 'Trailers', 'Motor Cycles', 'Other vehicles'])
            # show the graph
            plt.show()

        elif int(user_graph_choice) == 2:
            # total amount of vehicles registered
            plt.bar(vehicle_registration_df.Period,
                    vehicle_registration_df.Total)
            plt.xlabel("Years")
            plt.ylabel("Total amount of Vehicles Registered")
            plt.show()

        elif int(user_graph_choice) == 3:
            break

        else:
            print("invalid choice")
            continue


def year_view():
    ''' outputs a single year's data '''

    while True:
        ask_user_for_year = (input("\nPlease enter a year :"))

        # incorrect year check/isdecimal() returns true if only numbers are entered
        if not ask_user_for_year.isdecimal():
            print("\nEnter numbers only")

        elif 2000 > int(ask_user_for_year) or int(ask_user_for_year) > 2018:
            print("\nIncorrect Year")
            continue
        else:
            break
        # find data for the year entered
    custom_year = vehicle_registration_df[vehicle_registration_df.Period ==
                                          ask_user_for_year]
    # print the data
    print(custom_year.to_string(index=False))
    # ask if they want to search again


def year_vs_year():
    '''shows the difference between two years and produces a graph that shows the two years side by side'''
    df = vehicle_registration_df
    while True:
        year1_ask = input("Enter the 1st year :")
        # incorrect year check/isdecimal() returns true if only numbers are entered
        if not year1_ask.isdecimal():
            print("\nEnter numbers only")
        elif 2000 > int(year1_ask) or int(year1_ask) > 2018:
            print("\nIncorrect Year")
            continue
        else:
            break

    while True:
        year2_ask = input("\nEnter the 2nd year :")
        # incorrect year check/isdecimal() returns true if only numbers are entered
        if not year2_ask.isdecimal():
            print("\nEnter numbers only")
        elif 2000 > int(year2_ask) or int(year2_ask) > 2018:
            print("\nIncorrect Year")
            continue
        else:
            break

    year1 = df[df.Period == year1_ask
               ]
    year2 = df[df.Period == year2_ask
               ]

    # combine two years into 1 df
    joined_df = [year1, year2]
    joined_df = pd.concat(joined_df)
    # copy values here for the graph
    graph_values = joined_df
    # get the difference of the two years , .abs (absolute value) to get the absolute values and not negatives
    difference = joined_df.set_index("Period").diff().abs()
    # only show the difference in a single row
    difference = difference.iloc[1:2]
    # combime the row with the difference to the df with the years
    joined_df = [joined_df, difference]
    joined_df = pd.concat(joined_df)
    # because the index was set to 'period' ,the column goes blank when merged,so we can replace that NaN value with 'Difference' :),Perfect
    joined_df = joined_df.fillna('Difference')
    # print the data
    print('\n', joined_df.to_string(index=False))
    # plot graphs of the two years
    graph_values.plot.bar(x='Period')
    # labels
    plt.xlabel("Years")
    plt.ylabel("Amount of Vehicles Registered")
    # show the graph
    plt.show()


def prompt():

    while True:
        print(
            "\nTo view all the registration data from the year 2000 to 2018 Enter [1]\nTo view data by year Enter [2]\nTo view graphs of the data Enter [3]\nTo view summaries of the data Enter [4]\nTo compare two years Enter [5]\nTo exit the program Enter [0] ")
        ask_user = input('Choice : ')

        if not ask_user.isdecimal():
            print("\nEnter numbers only")
        elif int(ask_user) == 1:
            print(vehicle_registration_df.to_string(index=False))

        elif int(ask_user) == 2:
            year_view()

        elif int(ask_user) == 3:
            graphs()
        elif int(ask_user) == 4:
            summaries()
        elif int(ask_user) == 5:
            year_vs_year()
        elif int(ask_user) == 0:
            break
        else:
            print("\nIncorrect entry")
            continue


# run
prompt()
