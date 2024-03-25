import functools
import json
import yaml
import xml.etree.ElementTree as ET
import random


def to_format(format=None):
    """
    A decorator that converts the result of a function to a given format
    :param format: a string containing the requested format
    :return: the function that transformed the function
    """
    def decorator(function):
        """
        :param function: wrapped function
        :return: function that transforms
        """
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            """
            :param args: function parameters
            :param kwargs: default function parameters
            :return: function that returns the requested format
            """
            result = function(*args, **kwargs)

            if format is None:
                modified_result = json.dumps(result, indent=4)

            if format == 'xml':
                filename = f'{function.__name__}.xml'
                root = ET.Element("root")
                child = ET.Element("child")
                child.text = str(result)
                root.append(child)

                modified_result = ET.ElementTree(root)
                modified_result.write(filename)

            if format == 'yaml':
                modified_result = yaml.dump(result)

            return modified_result
        return wrapper
    return decorator


@to_format()
def printer(**kwargs):
    """
    :param kwargs: unlimited number of parameters
    :return: unpacked received object
    """
    return kwargs


@to_format('yaml')
def winner(**kwargs):
    """
    The function returns the winner of the draw
    :param kwargs: unlimited number of parameters
    :return: random dictionary key value
    """
    lucky = []
    for key, val in kwargs.items():
        lucky.append(random.choice(val))
    return lucky


user = {'UserName': 'Alice',
        'Password': 'star123*',
        'Room number': 237,
        'Hobbys': ('Fencing', 'Horseback riding', 'Modeling')}

raffle = {'Participants': ['Alice', 'Maria', 'Kiril']}

print(printer(**user))
print(winner(**raffle))
