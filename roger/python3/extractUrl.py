"""
Suppose any line of text can contain at most one url that starts with
“http://” and ends at the next space in the line. Write a fragment of
code to extract and print the full url if it is present.
"""


def extract_url(sentence):
    str_sentence = str(sentence)
    initial_pos = int(str_sentence.find("http://"))
    return str_sentence[initial_pos: str_sentence.find(" ", initial_pos)]


print(extract_url("Hello my friends, my site is http://www.very-very-friends.com.org I wait for you, visit me."))
