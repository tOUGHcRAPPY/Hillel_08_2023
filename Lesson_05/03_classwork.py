import time
from functools import lru_cache


def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


begin = time.time()
fib_without_cache(30)
end = time.time()

print(f"Fibonacci without cache: {fib_without_cache}")
print(f"Time taken without cache: {end - begin} seconds")


@lru_cache(maxsize=None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)


begin = time.time()
fib_without_cache(30)
end = time.time()

print(f"Fibonacci with cache: {fib_without_cache}")
print(f"Time taken with cache: {end - begin} seconds")
