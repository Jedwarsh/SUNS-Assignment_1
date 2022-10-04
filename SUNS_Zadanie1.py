import pandas as pd  # Importing pandas data frame module
import datetime      # Importing datetime module for easy date manipulation
import random        # Importing random module

# Reading the training and testing data
test_data = pd.read_csv('Z1-data/test.csv')
train_data = pd.read_csv('Z1-data/train.csv')


# CHANGING THE TYPE OF THE RELEASE DATE
def date_working(data):
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


train_data = number_of_player(train_data)
train_data = date_working(train_data)
print("asd")