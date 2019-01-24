filter = {}
filter.update({'children': 12})
filter.update({'teenager': 17})
filter.update({'young': 29})
filter.update({'greater': 30})

children = "You are a child"
teenager = "You are teenager"
young = "You are young"
greater = "You are greater"

def you_are(my_old):
    print((((lambda: greater, lambda: young)[my_old > filter.get('teenager') and my_old <= filter.get('young')]
           , lambda: teenager)[my_old > filter.get('children') and my_old <= filter.get('teenager')]
           , lambda: children)[my_old <= filter.get('children')]())

you_are(11)


you_are(15)


you_are(21)


you_are(30)


