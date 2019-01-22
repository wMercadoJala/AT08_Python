def operation(s, s1, s2):
    if s is "+":
        print(int(s1) + int(s2))
    elif s is "-":
        print(int(s1) - int(s2))
    elif s is "*":
        print(int(s1) * int(s2))
    elif s is "/":
        print(int(s1) / int(s2))


operation("*", "5", "6")
operation("+", "5", "6")
operation("-", "10", "2")
operation("/", "35", "7")
