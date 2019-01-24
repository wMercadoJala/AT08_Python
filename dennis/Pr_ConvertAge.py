def convert_age_to_days(age):
    return age * 365


def convert_age_to_hours(age):
    return convert_age_to_days(age) * 24


def convert_age_to_minutes(age):
    return convert_age_to_hours(age) * 60
