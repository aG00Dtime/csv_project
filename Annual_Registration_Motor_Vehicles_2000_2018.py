# Your python program must accomplish the following:

# Read selected data file and output its content
# out put the rows
# Output statistical summaries of the data file. You will decide on what summaries are appropriate and useful
# average amount of vehicles registered  per year and the total amount registeed from 2000 to 2018

# Produce at least 2 graphs on some aspect of the dataset. You will decide what graphs/charts you will produce
# graph of the cars registed over the years and the total number per year

# Perform and output results of comparative statistical analyses of the data of any two of the years of data available in your dataset
# compare the 1st year and the last year

# Perform Any ONE other creative analysis of some aspect of the data in the dataset.
# idk


# to do
# print the rows-done
# summaries- kinda?
# graphs -done
# compare
# idk

# <--- code STARTS here --->


import pandas as pd
import matplotlib.pyplot as plt


# <----Csv file handling starts here---->

# read the csv file
csv_file = pd.read_csv(
    "Annual_Registration_Motor_Vehicles_2000_2018.csv")

# only select the rows we want to use
vehicle_registration_df = csv_file.iloc[0:19]

# disables the warming when we change the data from str to ints
pd.options.mode.chained_assignment = None

# converts the values in the df to  int
for row in vehicle_registration_df:

    vehicle_registration_df[row] = vehicle_registration_df[row].astype(int)
    # print(str(vehicle_registration_df[row]))

# make the year column a str so it doesnt break the  year filter and graphs
vehicle_registration_df.Period = vehicle_registration_df.Period.astype(str)

# replace spaces in header names with underscores
vehicle_registration_df.columns = [col.replace(
    " ",  "_") for col in vehicle_registration_df.columns]

# <----Csv file handling ends here---->


def summaries():
    # summaries
    print("\nThe Average amount of Private cars registered per year was ",
          round(vehicle_registration_df.Private_Cars.mean(), 1), 'and the total amount registered was', vehicle_registration_df.Private_Cars.sum(), '.')


def graphs():
    # view graphs
    while True:
        print("To view a graphs that shows all registered vehicles during the period 2000 - 2018 Press 1\nTo view a graph that compares the total vehicles registerd per year during the period 2000 to 2018 Press 2\nTo exit this menu press 3")
        user_graph_choice = input("Choice : ")

        if int(user_graph_choice) == 1:

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
            # motorsycles
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
            plt.plot(vehicle_registration_df.Period,
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
    # view by year
    while True:
        ask_user_for_year = (input("Please enter a year :"))
        # print(type(ask_user_for_year))
        custom_year = vehicle_registration_df[vehicle_registration_df.Period ==
                                              ask_user_for_year]

        print(custom_year)
        user_go_again = input(
            "\nWould You like to enter another year? [Y]es,[N]o : ")
        if user_go_again.lower() == 'y':
            continue
        elif user_go_again.lower() == 'n':
            break
        else:
            continue


def prompt():
    # ask user what to do
    while True:
        print("\nTo view all the registration data from the year 2000 to 2018 Enter 1\nTo view data by year Enter 2\nTo view graphs of the data Enter 3\nTo view summaries of the data Enter 4\nTo exit the program Enter 0 ")
        ask_user = input('Choice : ')
        if int(ask_user) == 1:
            print(vehicle_registration_df)

        elif int(ask_user) == 2:
            year_view()

        elif int(ask_user) == 3:
            graphs()
        elif int(ask_user) == 4:
            summaries()
        elif int(ask_user) == 0:
            break
        else:
            print("\nincorrect entry")
            continue


# run
prompt()


# removed
# some columns are not in the right data type/have random characters so this is the way i remove them
# remove any numbers in the header
# vehicle_registration_df.columns = vehicle_registration_df.columns.str.replace(
#     '\d+', '').str.strip()
# def convert_column_types():
#     pd.options.mode.chained_assignment = None
#     vehicle_registration_df["Private_Cars"] = vehicle_registration_df["Private_Cars"].str.replace(
#         ",", "").astype(int)
#     vehicle_registration_df["Lorries"] = vehicle_registration_df["Lorries"].str.replace(
#         ",", "").astype(int)
#     vehicle_registration_df["Vans"] = vehicle_registration_df["Vans"].str.replace(
#         ",", "").astype(int)
#     vehicle_registration_df["Station_Wagons"] = vehicle_registration_df["Station_Wagons"].str.replace(
#         ",", "")
#     vehicle_registration_df["Station_Wagons"] = vehicle_registration_df["Station_Wagons"].str.replace(
#         "-", "0").astype(
#         int)
#     vehicle_registration_df["Motorcycles"] = vehicle_registration_df["Motorcycles"].str.replace(
#         ",", "").astype(int)
#     vehicle_registration_df["Other"] = vehicle_registration_df["Other"].str.replace(
#         ",", "").astype(int)
#     vehicle_registration_df["Total"] = vehicle_registration_df["Total"].str.replace(
#         ",", "").astype(int)
# .str.replace(
#     ",", "").astype(int)

# replace stuff with for loop
# for row in vehicle_registration_df:

# vehicle_registration_df[row] = vehicle_registration_df[row].str.replace(
#         ",", "").astype(int)
