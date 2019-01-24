"""
Create 1 module to Calculate age in minutes, hours and days
"""


def to_days(age):
    return age * 365


def to_hours(age):
    return age * 365 * 24


def to_minutes(age):
    return age * 365 * 24 * 60

print(to_days(32))
