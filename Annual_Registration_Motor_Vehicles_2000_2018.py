# Your python program must accomplish the following:

# Read selected data file and output its content and output the rows

# Output statistical summaries of the data file. You will decide on what summaries are appropriate and useful


# Produce at least 2 graphs on some aspect of the dataset. You will decide what graphs/charts you will produce


# Perform and output results of comparative statistical analyses of the data of any two of the years of data available in your dataset


# Perform Any ONE other creative analysis of some aspect of the data in the dataset.


# to do
# print the rows-done
# summaries- done,kinda?
# graphs -done
# compare-to do
# idk-?

# <--- code STARTS here --->

# import libs needed
import pandas as pd
import matplotlib.pyplot as plt


# <----Csv file handling starts here---->
# read the csv file
csv_file = pd.read_csv(
    "Annual_Registration_Motor_Vehicles_2000_2018.csv")

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


def summaries():
    # summaries
    # adds thousands seperator
    pd.options.display.float_format = '{:,.0f}'.format

    # print summaries
    print("\nAVERAGE VEHICLES (BY TYPE) REGISTERED PER YEAR FROM 2000 - 2018\n")
    print(vehicle_registration_df[['Private_Cars', 'Hire_Cars', 'Lorries', 'Buses',
                                   'Station_Wagons', 'Vans', 'Tractors', 'Trailers', 'Motorcycles', 'Other']].mean().to_string())
    # converted to float because base values are ints
    print("\nTOTAL VEHICLES (BY TYPE) REGISTERED FROM 2000 - 2018\n ")
    print(vehicle_registration_df[['Private_Cars', 'Hire_Cars', 'Lorries', 'Buses',
                                   'Station_Wagons', 'Vans', 'Tractors', 'Trailers', 'Motorcycles', 'Other']].sum().astype(float).to_string())  

    print("\nTOTAL VEHICLES REGISTERED FROM 2000 - 2018\n ")
    # converted to float because base values are ints
    print((vehicle_registration_df[['Total']].sum().astype(float).to_string()))


def graphs():
    # view graphs
    while True:
        print(
            "\nTo view a graphs that shows all registered vehicles during the period 2000 - 2018 Press [1]\nTo view a graph that compares the total vehicles registered per year during the period 2000 to 2018 Press [2]\nTo exit this menu press [3]")
        user_graph_choice = input("Choice : ")

        if int(user_graph_choice) == 1:
            # plot.bar plots everthing in the dataframe next to eachother
            # vehicle_registration_df.plot.bar()

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
    # view by year
    while True:
        ask_user_for_year = (input("\nPlease enter a year :"))

        # incorrect year check/isdecimal() returns true if only numbers are entered
        if not ask_user_for_year.isdecimal():
            print("Enter numbers only")

        elif 2000 > int(ask_user_for_year) or int(ask_user_for_year) > 2018:
            print("Incorrect Year")
            continue
        else:
            break
        # find data for the year entered
    custom_year = vehicle_registration_df[vehicle_registration_df.Period ==
                                          ask_user_for_year]
    # print the data
    print(custom_year)
    # ask if they want to search again
    while True:
        user_go_again = input(
            "\nWould You like to enter another year? [Y]es,[N]o : ")
        if user_go_again.lower() == 'y':
            year_view()
        elif user_go_again.lower() == 'n':
            break
        else:
            continue


def prompt():
    # ask user what to do
    while True:
        print(
            "\nTo view all the registration data from the year 2000 to 2018 Enter [1]\nTo view data by year Enter [2]\nTo view graphs of the data Enter [3]\nTo view summaries of the data Enter [4]\nTo exit the program Enter [0] ")
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
