
def basic_calculator(number_1, number_2, operation):
    if (number_1.isnumeric() & number_2.isnumeric()):
        number_1 = float(number_1)
        number_2 = float(number_2)
        if operation == "add":
            result = number_1 + number_2
        elif operation == "subtract":
            result = number_1 - number_2
        elif operation == "divide":
            result = number_1 / number_2
        elif operation == "multiply":
            result = number_1 * number_2
        else:
            result = "Operations supported: add, subtract, divide, multiple only"

    else:
        result = "Please enter a valid number for a & b"

    return result