# Author : Mitrovic Nikola
# Date : 15/06/2020

def operation(a):
    def add(b):
        return a+b
    return add

fn = operation(5)
print(fn)
print(fn(8))

def mean():
    count = 0
    total = 0
    def meanOp(n):
        nonlocal count, total
        total += n
        count += 1
        return total/count
    return meanOp

fn2 = mean()
print(fn2(5))