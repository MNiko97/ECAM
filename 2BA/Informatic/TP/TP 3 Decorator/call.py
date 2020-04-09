def hello ():
    print('hello')

def call(func):
    return func()

def add(a, b):
    return a + b

def call_2(func, *args):
    return func(*args) 

def sub(a, b):
    return a - b

def call_3(func, *args, **kwargs):
    return func(*args, **kwargs)

def compute(a, b, op=add):
    return op(a, b)
    
print(call_3(compute, 2, 9))
print(call_3(compute, 2, 9, op=sub))