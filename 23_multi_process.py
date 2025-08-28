import os
import multiprocessing
import time

def cat(num, name):
    print(f'cat pid: {os.getpid()}')
    print(f'cat ppid: {os.getppid()}')
    for i in range(num):
        print(f'cat: {name}, is running')
        time.sleep(1)

def dog(num, name):
    print(f'dog pid: {os.getpid()}')
    print(f'dog ppid: {os.getppid()}')
    for i in range(num):
        print(f'dog: {name}, is running')
        time.sleep(1)        


if __name__ == '__main__':
    print(f'main process, pid: {os.getpid()}')

    cat_process = multiprocessing.Process(target = cat, args = (3, '银渐层'), daemon = True)
    dog_process = multiprocessing.Process(target = dog, kwargs = { 'num': 2, 'name': '边牧'})

    # 设置 daemon 成为守护进程，当主进程结束时，所有 daemon 子进程会被强制杀死，不会等它们跑完
    # dog_process.daemon = True

    cat_process.start()
    dog_process.start()

    # 不管是否 join，主进程都会等待子进程，区别就是想要拿到结果必须要 join



