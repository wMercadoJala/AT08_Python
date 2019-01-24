def replace(string_in, old_string, new_string):
    list_string = string_in.split(old_string)
    return new_string.join(list_string)


print(replace("Mississipi", "i", "I"))
print(replace("I love spom! Spom is my favorite food. Spom, spom, yum!", "om", "am"))
