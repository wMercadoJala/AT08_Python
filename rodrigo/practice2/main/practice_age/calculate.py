def age(age_number):
    days = age_number * 365
    hours = days * 24
    minutes = hours * 60
    base_print = "Your age in days is: {0} days\nYour age in hours is: {1} hours\nYour age in minutes is: {2} minutes"
    return base_print.format(days, hours, minutes)