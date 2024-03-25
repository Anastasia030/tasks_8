import json


def to_json(function):
    """
    A decorator that converts the result of a function to json format
    :param function: wrapped function
    :return: function that transforms
    """
    def wrapper(*args, **kwargs):
        """
        :param args: function parameters
        :param kwargs: default function parameters
        :return: function that returns to the format json
        """
        result = function(*args, **kwargs)
        modified_result = json.dumps(result, indent=4)

        return modified_result
    return wrapper


@to_json
def printer(**kwargs):
    """
    The function outputs a string with the characteristics of the employee
    :param kwargs: indefinite dictionary size
    :return: string with modified variables
    """
    for key, val in kwargs.items():
        return f'Name: {key}, Age: {val[0]}, Work experience: {val[1]}'


@to_json
def simple_number(number):
    """
    The function checks whether the number is prime
    :param number: any number
    :return: Boolean value
    """
    count = 0
    for i in range(1, int(number ** 0.5)+1):
        if number % i == 0:
            count += 1
    if count > 1:
        return False
    return True


@to_json
def survey(**kwargs):
    """
    The function returns the results of the survey
    :param kwargs: unlimited number of parameters
    :return: dictionary line by line
    """
    questionnaire = {}
    for key, val in kwargs.items():
        questionnaire[key] = val
    return questionnaire


working_staff = {'Ivanov': [34, 7], 'Smirnov': [29, 3], 'Petrov': [21, 1]}
print(printer(**working_staff))
print(simple_number(11))
print(survey(Name='Valentin', Age='25', Profession='Cook'))