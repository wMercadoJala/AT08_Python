"""
Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
Example: replace("Mississippi", "i", "I") == "MIssIssIppI"

"""


def replace_in_text(text, old, new):
    str_text = str(text)
    return str_text.replace(old, new)


print(replace_in_text("Mississippi", "i", "I"))
print(replace_in_text("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am"))
print(replace_in_text("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a"))
