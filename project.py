
# Your python program must accomplish the following:

# Read selected data file and output its content
# out put the rows
# Output statistical summaries of the data file. You will decide on what summaries are appropriate and useful

# Produce at least 2 graphs on some aspect of the dataset. You will decide what graphs/charts you will produce

# Perform and output results of comparative statistical analyses of the data of any two of the years of data available in your dataset

# Perform Any ONE other creative analysis of some aspect of the data in the dataset.

# <--- code STARTS here --->
import csv
import matplotlib as plt


def country_specific_csv():
    # list to hold extracted date from the datasheet
    a_country = []

    #   READ CSV
    with open("covid.csv", 'r') as csv_file:
        # convert to dict to read by keys
        csv_dict_reader = csv.DictReader(csv_file)

        # parse data we want from the larger datasheet
        # go through the rows and filter

        user_country = input("Please enter a country to output data for :")
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
                    'date': row['date'],
                    # "country": row['location'],
                    'new_cases': row['new_cases'],
                    'new_deaths': row['new_deaths'],
                    'total_deaths': row['total_deaths']


                })

    # write new csv with the selected data from the old csv
    # create new csv file called country.csv with our extracted data
    # file name depends on the chosen country
    with open(user_country.capitalize() + '.csv', 'w', newline='') as a_country_csv:
        fieldnames = ['date',  'new_cases',  # 'country',
                      'new_deaths', 'total_deaths']
        csv_dict_writer = csv.DictWriter(a_country_csv, fieldnames=fieldnames)
        csv_dict_writer.writeheader()
        for selected_country in a_country:
            csv_dict_writer.writerow(selected_country)
    print("New csv file created.")


country_specific_csv()
# <--- code ENDS here --->
