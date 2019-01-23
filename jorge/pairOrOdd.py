def pair_or_odd(min, max, pairOdd):
    container = list(range(min, max))
    (lambda: get_odd(container), lambda: get_pair(container))[pairOdd == "pair"]()


def get_pair(container):
    for date in container:
        if date % 2 == 0: print(date)


def get_odd(container):
    for date in container:
        if date % 2 != 0: print(date)


pair_or_odd(1, 10, "pair")

