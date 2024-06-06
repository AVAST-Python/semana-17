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

def fibonacci(n, conn):
    if n <= 1:
        conn.send(n)
        conn.close()
        return
    parent_conn1, child_conn1 = multiprocessing.Pipe()
    parent_conn2, child_conn2 = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=fibonacci, args=(n-1, child_conn1))
    p2 = multiprocessing.Process(target=fibonacci, args=(n-2, child_conn2))
    p1.start()
    p2.start()
    result1 = parent_conn1.recv()
    result2 = parent_conn2.recv()
    conn.send(result1 + result2)
    conn.close()
    p1.join()
    p2.join()

@with_timer
def run_fibonacci(n):
    if n <= 1:
        return n
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=fibonacci, args=(n, child_conn))
    p.start()
    result = parent_conn.recv()
    p.join()
    return result

if __name__ == '__main__':
    # 20 short
    # 30 ok ~ 2-3
    # 35 ko ~ 28 s
    print(run_fibonacci(30))
