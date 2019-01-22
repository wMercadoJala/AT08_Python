days_of_month = {}
days_of_month.update({'January': 31})
days_of_month.update({'February': 28})
days_of_month.update({'March': 31})
days_of_month.update({'April': 30})
days_of_month.update({'May': 31})
days_of_month.update({'June': 30})
days_of_month.update({'July': 31})
days_of_month.update({'August': 31})
days_of_month.update({'September': 30})
days_of_month.update({'October': 31})
days_of_month.update({'November': 30})
days_of_month.update({'December': 31})


def days_in_month(day):
    return str(days_of_month[day]) if day in days_of_month else 'None'


print(days_in_month('May'))
print(days_in_month('February'))
print(days_in_month('September'))
print(days_in_month('Quintilis'))
