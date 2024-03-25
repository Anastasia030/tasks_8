def register(symbol):
    """
    :param symbol: line elements
    :return: uppercase characters
    """
    return symbol.isupper()


proposal = input()
first_number = int(input()) - 1
last_number = int(input())

print(list(filter(register, proposal[first_number:last_number+1])))
