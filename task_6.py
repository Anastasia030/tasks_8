def decorator(function):
    print(function(input()))
    return function


@decorator
def counter(text):
    count = 0
    for words in text.split():
        count += len(words)
    return count
