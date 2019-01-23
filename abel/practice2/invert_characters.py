def invert_characters(_sepator_, _unified_, string):
    return _unified_.join(str(string).split(_sepator_))


print(invert_characters("is", "IS", "misisipi"))
print(invert_characters("i", "I", "misisipi"))
