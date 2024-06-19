def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def raiz(num1, num2):
    return  num1 ** num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2

my_mapper = {
    "+": add,
    "-": sub,
    "^": raiz,
    "/": divide,
    "*": multiply,

}


def execute_expressions(exp):
    num1_text, sign, num2_text = exp.split()
    num1 = float(num1_text)
    num2 = float(num2_text)
    return my_mapper[sign](num1, num2)
