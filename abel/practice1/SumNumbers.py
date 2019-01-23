def sum(number):
    aux = 0
    for index in range(0, number + 1):
        if index < 35:
            aux += index
    return aux


print("total sum : "+str(sum(10)))

print("total sum : "+str(sum(44)))