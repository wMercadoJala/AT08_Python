calendar = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
            'September': 30, 'October': 31, 'November': 30, 'December': 31}


def days_in_month(month):
    """
    This method ask if the month exist in the calendar and return the number of days.
    :param month: Input month.
    :return: The days of the month.
    """
    if month not in calendar:
        return "Error, please check the input"
    return calendar[month]
