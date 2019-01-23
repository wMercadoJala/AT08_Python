def replace(phrase, old, new):
    print(new.join(phrase.split(old)))


replace("Missisipi", "i", "o")
song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
replace(song, "om", "am")
replace(song, "o", "a")
