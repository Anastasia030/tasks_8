from datetime import datetime
import functools


def exceptional_situations(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
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
    count = 0
    number_new = int(number)
    for i in range(1, int(number_new ** 0.5)+1):
        if number_new % i == 0:
            count += 1
    if count > 1:
        return False
    return True


print(simple_number(input()))

