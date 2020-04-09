def binrep(n):
    while n != 0:
        bit = n%2
        n //=2
        yield bit

# b = binrep(12)
# while True:
#     try:
#         print(next(b))
#     except:
#         StopIteration
#         break

class NaturalIterator:
    def __init__(self, n):
        self.__n  = n
        self.__generator = binrep(n)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__generator)

    def __getitem__(self, i):
        if i**2 > self.__n:
            raise IndexError()
        return self.__n%(i**2)

class Natural:
    def __init__(self, n):
        self.__iterable = binrep(n)

    def __iter__(self):
        return self.__iterable

for e in Natural(42):
    print(e)