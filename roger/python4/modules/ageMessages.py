"""
Create 1 modules to print 4 different messages :
    - You are a child, when the age is lower than 12
    - Your are teenager, when the age is between 13 and 17
    - You are young, when the age is between 18 and 29
    - You are adult, when the age is greater than 30

"""


def people_is(age):
    ages_people = {1: {'age_min': 0, 'age_max': 12, 'people': 'child'},
                   2: {'age_min': 13, 'age_max': 17, 'people': 'teenager'},
                   3: {'age_min': 18, 'age_max': 29, 'people': 'young'},
                   4: {'age_min': 30, 'age_max': 1000, 'people': 'adult'}}
    for key in ages_people:
        if ages_people[key]['age_min'] <= int(age) <= ages_people[key]["age_max"]:
            return ages_people[key]['people']
