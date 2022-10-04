import pandas as pd  # Importing pandas data frame module
import datetime      # Importing datetime module for easy date manipulation
import random        # Importing random module

# Reading the training and testing data
test_data = pd.read_csv('Z1-data/test.csv')
train_data = pd.read_csv('Z1-data/train.csv')


# CHANGING THE TYPE OF THE RELEASE DATE
def date_int_form(data):

    # Filling up the NaN values
    data["D_release_date"] = data["D_release_date"].fillna("1 Jan, 2001")

    for i in range(data["D_release_date"].size):

        # Splitting up the date
        split_up_date = data["D_release_date"].iloc[i].split()

        # If the months and days are in the wrong order we switch them
        if len(split_up_date[0]) > 2 and len(split_up_date) > 2:
            split_up_date[0], split_up_date[1] = split_up_date[1], split_up_date[0]

        # Getting the corresponding number for a given month with datetime module
        month_name = split_up_date[-2].strip(",")
        datetime_object = datetime.datetime.strptime(month_name, "%b")
        month_number = datetime_object.month

        # Producing the final integer value with or without days
        if len(split_up_date[0]) <= 2:
            data_int_form = int(split_up_date[-1]) * 10000 + (month_number * 100) + int(split_up_date[0])
        else:
            data_int_form = int(split_up_date[-1]) * 10000 + (month_number * 100) + int(14)

        # Replacing the string value with a new integer value
        data["D_release_date"].iloc[i] = data_int_form

    # Returning the reformatted data frame
    return data


# CHANGING THE TYPE OF THE NUMBER OF OWNERS
def number_of_player(data):

    for i in range(data["D_owners"].size):

        # Splitting up the number of owners
        split_up_data = data["D_owners"].iloc[i].split()

        # Changing the type of the minimum/maximum number of owners
        min_value = int(split_up_data[0].replace(',', ''))
        max_value = int(split_up_data[-1].replace(',', ''))

        # Creating a random number between the minimum and maximum
        new_value = random.randint(min_value, max_value)

        # Replacing the string value with a new integer value
        data["D_owners"].iloc[i] = new_value

    # Returning the reformatted data frame
    return data


# CONVERTING THE GENRES INTO INTEGER FORM
def convert_genres(data):

    # Filling up the NaN values
    data["D_genre"] = data["D_genre"].fillna("Action")

    # Getting every possible combination of genres
    x = data["D_genre"].unique()

    # Getting every single type of genre
    y = []
    types = []
    for i in range(len(x)):
        y.append(x[i].split(','))
        for j in range(len(y[i])):
            types.append(y[i][j].replace(' ', ''))

    # Removing duplicates and sorting the list
    types = list(set(types))
    types.sort()

    for i in range(data["D_genre"].size):

        # Creating necessary variables
        genre_number = ""
        genre_int = 0

        # Splitting up the data for a specific game
        genre_str_split = data["D_genre"].iloc[i].split(',')

        for j in range(len(genre_str_split)):

            # Removing spaces from genre names
            genre_str_split[j] = genre_str_split[j].replace(' ', '')

            # Storing the genres in numerical format but in a string
            genre_number += str(types.index(genre_str_split[j]))

            # Converting the string into integer
            if j == len(genre_str_split)-1:
                genre_int = int(genre_number)

            # Adding a 0 between genres to easily distinguish them
            else:
                genre_number += "0"

        # Replacing the string value with a new integer value
        data["D_genre"].iloc[i] = genre_int

    # Returning the reformatted data frame
    return data


# Removing useless columns
train_data = train_data.drop(['D_appid', 'D_reviews', 'has_website_linked', 'coming_soon'], axis=1)

# Removing rows with NaN values
train_data = train_data.dropna()

train_data = convert_genres(train_data)

train_data = number_of_player(train_data)

train_data = date_int_form(train_data)

print("asd")