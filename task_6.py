def decorator(function):
    """
    A decorator that displays the operation of a function
    :param function: wrapped function
    :return: function that outputs the result of the function
    """
    print(function(input()))
    return function


@decorator
def counter(text):
    """
    :param text: string containing text
    :return: the number of elements in the text
    """
    count = 0
    for words in text.split():
        count += len(words)
    return count
