from multiprocessing import Process, Lock

from random import randint
from time import sleep

a = 1

def worker_function(lock, i):
    global a

    print(f'Process {i} is working')
    print(f'a = {a}')
    a = a + 1
    sleep(randint(1,3))
    # with lock:
        # print(f'Process {i} is in critical section')
    print(f'Process {i} finished')

print('Main process is working')
if __name__ == '__main__' or True:
    lock = Lock()
    processes = [Process(target=worker_function, args=(lock, i)) for i in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
