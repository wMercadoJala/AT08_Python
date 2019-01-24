filter = {}
filter.update({'minutes': 60})
filter.update({'hours': 60})
filter.update({'days': 365})


def age_in(minut_hour_days):
    print(((lambda: get_age_in_days(), lambda: get_age_in_hours())[minut_hour_days == 'hours'], lambda: get_age_in_minutes())[minut_hour_days == 'minutes']())


def get_age_in_hours():
    return filter.get('hours')*filter.get('days')


def get_age_in_minutes():
    return filter.get('minutes')*filter.get('hours')*filter.get('days')


def get_age_in_days():
    return filter.get('days')


age_in('minutes')
age_in('hours')
age_in('days')