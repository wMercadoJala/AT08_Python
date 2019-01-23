def operation_numbers(sign_op, num1, num2):
    if sign_op is "+":
        print(int(num1) + int(num2))
    elif sign_op is "-":
        print(int(num1) - int(num2))
    elif sign_op is "*":
        print(int(num1) * int(num2))
    elif sign_op is "/":
        print(int(num1) / int(num2))
    elif sign_op == "**":
        print(int(num1) ** int(num2))
    elif sign_op == "//":
        print(int(num1) // int(num2))


operation_numbers("+", "10", "3")
operation_numbers("-", "15", "5")
operation_numbers("*", "5", "8")
operation_numbers("/", "36", "6")
operation_numbers("//", "15", "2")
operation_numbers("**", "2", "3")
