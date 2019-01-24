def count_letters_dic(cad):
    cad = str(cad).lower().replace(" ", "")
    counter = {}
    for letter in cad:
        counter.update({letter: counter[letter] + 1 if letter in counter else 1})
    for elem in sorted(counter.keys()):
        print(elem, counter[elem])
    print("")


count_letters_dic("Practice")
count_letters_dic("Tres tristes tigres trillan trigo en un trigal")
count_letters_dic("ThiS is String with Upper and lower case Letters")
