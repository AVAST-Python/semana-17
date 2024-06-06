from functools import lru_cache

def with_timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end-start}")
        return result
    return wrapper

@lru_cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@with_timer
def run_fibonacci(n):
    return fibonacci(n)

if __name__ == '__main__':
    # 20 short
    # 30 ok ~ 2-3
    # 35 ko ~ 28 s
    print(run_fibonacci(30))
