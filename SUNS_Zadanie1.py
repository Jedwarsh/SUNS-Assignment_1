import pandas as pd  # Importing Pandas Data Frame module
import datetime  # Importing datetime module for easy date manipulation

# Reading the training and testing data
test_data = pd.read_csv('Z1-data/test.csv')
train_data = pd.read_csv('Z1-data/train.csv')

# CHANGING THE TYPE OF THE RELEASE DATE
# Filling up the NaN values
train_data["D_release_date"] = train_data["D_release_date"].fillna("1 Jan, 2001")

for i in train_data["D_release_date"]:
    # Splitting up the date
    split_up_date = i.split()

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
        data_int_form = int(split_up_date[-1]) * 10000 + (month_number * 100)

print(train_data.head(8))
