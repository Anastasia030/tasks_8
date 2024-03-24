import functools
import json
import yaml
import xml.etree.ElementTree as ET
import random


def to_format(format=None):
    def decorator(function):

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
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
    return kwargs


@to_format('yaml')
def winner(**kwargs):
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