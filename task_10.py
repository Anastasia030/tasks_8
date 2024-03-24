import time


def limit(limit_time, max_calls, period):
    def decorator(func):
        last_reset = time.time()
        b = [last_reset]

        def wrapper(*args, **kwargs):
            call_count = 0

            if time.time() - b[0] >= period:
                b[0] = time.time()

            if call_count >= max_calls or time.time() - last_reset > limit_time:
                raise Exception('TIMES OUT!')

            call_count += 1

            return func(*args, **kwargs)
        return wrapper
    return decorator


@limit(3, 4, 4)
def print_stairs(size):
    if size > 0:
        print('*' * size)
        time.sleep(2)

        print_stairs(size - 1)


print_stairs(10)