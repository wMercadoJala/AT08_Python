def operation(sign_op, num1, num2):
    if sign_op is "+":
        print(int(num1) + int(num2))
    elif sign_op is "-":
        print(int(num1) - int(num2))
    elif sign_op is "*":
        print(int(num1) * int(num2))
    elif sign_op is "/":
        print(int(num1) / int(num2))


operation("*", "5", "6")
operation("+", "5", "6")
operation("-", "10", "2")
operation("/", "35", "7")
