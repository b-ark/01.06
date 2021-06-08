# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


def make_operation(operator, *args):
    # проверка каждого элемента кортежа на тип данных int и float
    for item in args:
        if not isinstance(item, (int, float)):
            return None
    result = args[0]
    if operator == '+':
        result = sum(item for item in args)
    elif operator == '-':
        for i in range(1, len(args)):
            result -= args[i]
    elif operator == '*':
        for i in range(1, len(args)):
            result *= args[i]
    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
