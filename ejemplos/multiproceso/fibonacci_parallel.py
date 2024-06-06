import multiprocessing

def with_timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end-start}")
        return result
    return wrapper

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def run_fibonacci_child(n, conn):
    result = fibonacci(n)
    conn.send(result)
    conn.close()

@with_timer
def run_fibonacci(n):
    if n <= 1:
        return n

    parent_conn1, child_conn1 = multiprocessing.Pipe()
    parent_conn2, child_conn2 = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=run_fibonacci_child, args=(n-1, child_conn1))
    p2 = multiprocessing.Process(target=run_fibonacci_child, args=(n-2, child_conn2))

    p1.start()
    p2.start()

    result1 = parent_conn1.recv()
    result2 = parent_conn2.recv()

    p1.join()
    p2.join()

    return result1 + result2

if __name__ == '__main__':
    # 20 short
    # 30 ok ~ 2-3
    # 35 ko ~ 28 s
    print(run_fibonacci(35))
