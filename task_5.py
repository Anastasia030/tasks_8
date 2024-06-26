from functools import reduce


def multiply(first, second):
    """
    :param first: the first number
    :param second: the second number
    :return: multiplication of two numbers
    """
    return first * second


number_a, number_b, number_c = map(int, input().split())
print(reduce(multiply, filter(lambda x: x % number_c == 0 and x % (x ** 0.5) == 0, range(number_a, number_b + 1))))
