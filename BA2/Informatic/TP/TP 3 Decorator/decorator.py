import time

def delay(func):
    def wrapper(*args):
        func(*args)
        time.sleep(1)
    return wrapper

def delay_2(time_delay):
    def decorator(func):
        def wrapper(*args):
            func(*args)
            time.sleep(time_delay)
        return wrapper
    return decorator

@delay_2(2)
def printnum(i):
    print(i)

cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1

print('KA-BOOM ! ')

