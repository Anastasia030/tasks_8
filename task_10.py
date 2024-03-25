import time


def limit(limit_time, max_calls, period):
    """
    A decorator that causes an error after a specified time, or after a certain number
    of function launches within a certain period
    :param limit_time: number indicating seconds the function is executed
    :param max_calls: number indicating the number of calls for the specified period
    :param period: number indicating the time period in seconds for which the function can be called
    :return: the function that transformed the function
    """
    def decorator(function):
        """
        :param function: wrapped function
        :return: function that transforms
        """
        initial_time = time.time()
        start_time = [initial_time]
        call_count = [0]

        def wrapper(*args, **kwargs):
            """
            :param args: function parameters
            :param kwargs: default function parameters
            :return: artificially caused exception
            """

            if time.time() - start_time[0] >= period:
                start_time[0] = time.time()

            if call_count[0] >= max_calls or time.time() - initial_time > limit_time:
                raise Exception('TIMES OUT!')

            call_count[0] += 1

            return function(*args, **kwargs)
        return wrapper
    return decorator


@limit(3, 4, 4)
def print_stairs(size):
    """
    The function returns a ladder of asterisks
    :param size: number, the number of asterisks in the first line
    :return: row with a certain number of elements
    """
    if size > 0:
        print('*' * size)
        time.sleep(2)

        print_stairs(size - 1)


print_stairs(10)
