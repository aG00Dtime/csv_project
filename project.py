
# Your python program must accomplish the following:

# Read selected data file and output its content
# out put the rows
# Output statistical summaries of the data file. You will decide on what summaries are appropriate and useful

# Produce at least 2 graphs on some aspect of the dataset. You will decide what graphs/charts you will produce

# Perform and output results of comparative statistical analyses of the data of any two of the years of data available in your dataset

# Perform Any ONE other creative analysis of some aspect of the data in the dataset.

# <--- code STARTS here --->
import csv
from matplotlib import pyplot as plt
import pandas as pd

# <--- to do--->
print("This program outputs the cases,deaths and total Deaths of a population from the selected country ")
# create new file with data we want -done,kinda
# output the data -done,kinda
# graphs
# comparisons
# <------------>


def country_specific_csv():
    # list to hold extracted date from the datasheet
    a_country = []

    #   READ CSV
    with open("covid.csv", 'r') as csv_file:
        # convert to dict to read by keys
        csv_dict_reader = csv.DictReader(csv_file)

        # parse data we want from the larger datasheet
        # go through the rows and filter

        user_country = input("\nPlease enter a country to output data for :")
        # extract data
        for row in csv_dict_reader:
            # filter by country
            date = row['date']
            country = row['location']
            total_deaths = row['total_deaths']
            new_cases = row['new_cases']
            new_deaths = row['new_deaths']
            # append this dictionary of data to new list
            if country == user_country.capitalize():
                # print(date, country, new_cases,
                #       new_deaths, total_deaths)
                a_country.append({
                    'Date': row['date'],
                    # "country": row['location'],
                    'New_Cases': row['new_cases'],
                    'New_Deaths': row['new_deaths'],
                    # "Median_Age": row['median_age'],
                    # "65_and_older": row['aged_65_older'],
                    # "70_and_older": row['aged_70_older'],
                    'Life_Expectency': row['life_expectancy'],
                    'Population': row['population'],
                    'Total_Deaths': row['total_deaths']



                })

    # write new csv with the selected data from the old csv
    # create new csv file called country.csv with our extracted data
    # file name depends on the chosen country
    with open(user_country.capitalize() + '.csv', 'w', newline='') as a_country_csv:
        fieldnames = ['Date',  'New_Cases', 'New_Deaths',
                      'Life_Expectency', 'Population', 'Total_Deaths']
        csv_dict_writer = csv.DictWriter(a_country_csv, fieldnames=fieldnames)
        csv_dict_writer.writeheader()
        for selected_country in a_country:
            csv_dict_writer.writerow(selected_country)
    print("\nNew csv file created.")
    # ask how many rows to show from user
    #user_row_answer = input('how many rows of data would you like to view?')

    # TESTING TO SEE HOW THE THING WORKS  ---- TEMP
    pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_columns', None)
    new_file = pd.read_csv(user_country.capitalize() + '.csv')
    print(new_file)
    stat_answer = input(
        "\nwould you like a summary of the country? [Y]es , [N]o: ")
    if stat_answer.upper() != "N":
        print(new_file.describe())
    graph_answer = input(
        "\nWould you like to view a graph ? [Y]es, [N]o: ")
    if graph_answer != "N":
        plt.plot(new_file.Date, new_file.Total_Deaths)
        plt.show()
    # TESTING TO SEE HOW THE THING WORKS  ---- TEMP


country_specific_csv()
# <--- code ENDS here --->
