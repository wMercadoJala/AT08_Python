def order_dictionary(name_):
    name_ = str(name_).replace(" ", "").lower()

    dictionary_ = {}

    for valor in name_:
        dictionary_[valor] = name_.count(valor)
    return sorted(dictionary_.items())


print(order_dictionary("ThiS is String with Upper and lower case Letters"), "/n")
