from datetime import datetime
import functools


def exceptional_situations(function):
    """
    The decorator records exceptional situations and the time of their occurrence
    :param function: wrapped function
    :return: function that transforms
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        """
        The function that creates a file with the name of the exception and the time of its occurrence
        :param args: function parameters
        :param kwargs: default function parameters
        :return: string containing the name of the exception
        """
        try:
            return function(*args, **kwargs)

        except Exception as err:
            problem = type(err).__name__
            filename = f'{function.__name__}.txt'
            with open(filename, 'a') as file_exception:
                print(datetime.now(), problem, file=file_exception)
            return problem
    return wrapper


@exceptional_situations
def simple_number(number):
    """
    The function checks whether the number is prime
    :param number: any number
    :return: Boolean value
    """
    count = 0
    number_new = int(number)
    for i in range(1, int(number_new ** 0.5)+1):
        if number_new % i == 0:
            count += 1
    if count > 1:
        return False
    return True


print(simple_number(input()))
