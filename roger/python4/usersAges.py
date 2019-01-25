from roger.python4.modules import ageMessages
from roger.python4.modules import calculateAge

"""
Create a script importing both modules and performing de action :
 - Ask to the user the amount of users
 - For all users define the name and the age for each one, save this data as a dictionary 
 - After all users are defined, need to :
    - print the age in minutes, hours and days
    - The expected message according the age define

"""

users_dict = {}


def create_dictionary_user():
    """
    Method for create and fill a dictionary from keyboard.
    :return: new dictionary.
    """
    try:
        size = input("Insert number of users: ")

        global users_dict
        for i in range(int(size)):
            key = "User {0}".format(str(i + 1))
            users_dict[key] = {}
            users_dict[key]['name'] = input("  Insert name {0}: ".format(key))
            users_dict[key]['age'] = input("  Insert age {0}: ".format(key))
            while not users_dict[key]['age'].isdigit():
                print("Please insert a number int value.")
                users_dict[key]['age'] = input("  Insert age {0}: ".format(key))
    except ValueError:
        print("Please insert a number value.")


def show_age_users(my_dictionary):
    for user in my_dictionary:
        age = my_dictionary[user]['age']
        print(user, ":")
        print("          Name: ", my_dictionary[user]['name'])
        print("           Age: ", age)
        print("Age in minutes:", calculateAge.to_minutes(age))
        print("  Age in hours:", calculateAge.to_hours(age))
        print("   Age in days:", calculateAge.to_days(age))
        print("       User is:", ageMessages.people_is(age))


create_dictionary_user()
show_age_users(users_dict)
