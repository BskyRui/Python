import threading
import time

def cat(num, name):
    for i in range(num):
        print(f'cat: {name}, is running')
        time.sleep(0.5)

def dog(num, name):
    for i in range(num):
        print(f'dog: {name}, is running')
        time.sleep(1)        


if __name__ == '__main__':

    cat_thread = threading.Thread(target = cat, args = (3, '银渐层'), daemon = True)
    dog_thread = threading.Thread(target = dog, kwargs = { 'num': 2, 'name': '边牧'})

    # 设置 daemon 成为守护线程，当主进程结束时
    # 所有 daemon 子线程会被强制杀死，不会等它们跑完
    # dog_process.daemon = True

    cat_thread.start()
    dog_thread.start()

    # 不管是否 join，主线程都会等待子线程，区别就是想拿到结果必须要 join



