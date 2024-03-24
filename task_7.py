import json


def to_json(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        modified_result = json.dumps(result, indent=4)

        return modified_result
    return wrapper


@to_json
def printer(**kwargs):
    for key, val in kwargs.items():
        return f'Name: {key}, Age: {val[0]}, Work experience: {val[1]}'


@to_json
def simple_number(number):
    count = 0
    for i in range(1, int(number ** 0.5)+1):
        if number % i == 0:
            count += 1
    if count > 1:
        return False
    return True


@to_json
def survey(**kwargs):
    questionnaire = {}
    for key, val in kwargs.items():
        questionnaire[key] = val
    return questionnaire


working_staff = {'Ivanov': [34, 7], 'Smirnov': [29, 3], 'Petrov': [21, 1]}
print(printer(**working_staff))
print(simple_number(11))
print(survey(Name='Valentin', Age='25', Profession='Cook'))