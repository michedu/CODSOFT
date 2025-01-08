# addition
def add(n1, n2):
    return n1 + n2


# subtraction
def sub(n1, n2):
    return n1 - n2


# multiplication
def mul(n1, n2):
    return n1 * n2


# division
def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbols in operations:
        print(symbols)

    end = False

    while end is False:
        symbol_used = input("pick an operation : ")
        num2 = float(input("What's the next number?: "))
        oper = operations[symbol_used]
        ans = oper(num1, num2)
        print(f"{num1} {symbol_used} {num2} is = {ans}")
        cont = input(f"Do you want to continue calculating with {ans}? Type 'y' for yes,"
                     f"'b' for new calculation and 'n' for no: ")
        if cont == "y":
            num1 = ans
        elif cont == "b":
            end = True
            calculator()
        else:
            end = True


calculator()
