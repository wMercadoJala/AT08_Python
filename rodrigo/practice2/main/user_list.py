import random

names = ["Jose", "Arturo", "Walter", "Ariel", "Abel", "Dennis", "Nestor", "Wilson", "Roger", "Jorge", "Melvi",
         "Patricia", "Grace", "John", "Andy", "Joe"]


def create_list(names):
    """
    This method creates a list with length of 100 with all their names of the users.
    :param names: Input names.
    :return: A dictionary with the users.
    """
    dict_user = {}
    for item in range(100):
        dict_user[item + 1] = random.choice(names).lower()
    return dict_user


def request_user_id(number, dict_user):
    """
    This method request a user, with a input parameter.
    :param number: Input ID.
    :param dict_user: Input dictionary.
    :return: Return the id.
    """
    request = []
    if number > 9:
        print("Please, enter a single number")
        return request
    for item in dict_user.keys():
        if str(item)[0] == str(number):
            request.append(item)
    return request


def request_user_name(letter, dict_user):
    """
        This method request a user, with a input parameter.
        :param letter: Input letter.
        :param dict_user: Input dictionary.
        :return: Return the user name.
        """
    request = []
    if len(letter) != 1 or not letter.isalpha():
        print("Please, enter a single valid character")
        return request
    for item in dict_user.values():
        if letter == item[0]:
            request.append(item)
    return request


def user_group(user_num):
    """
    This method classify a user in to groups.
    :param user_num: Input username.
    :return: Group of the user.
    """
    if 1 <= user_num <= 25:
        return "The user belong Group 1"
    if 26 <= user_num <= 50:
        return "The user belong Group 2"
    if 51 <= user_num <= 75:
        return "The user belong Group 3"
    return "The user belong Group 4"


list_of_users = create_list(names)
print(list_of_users)
print(request_user_id(1, list_of_users))

print(request_user_name('w', list_of_users))
