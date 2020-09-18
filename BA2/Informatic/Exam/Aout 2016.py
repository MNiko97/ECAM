# Examen Aout 201T667

# Exercice 3 Expression régulière :
import re

matriculePattern = re.compile(r'[1-9]\d{4}')
datePattern = re.compile(r'(0[1-9]|[12]\d|3[01])/(0[1-9]|1[012])/[1-9]\d{3}')
pricePattern = re.compile(r'([1-9]\d+(\.\d+)?)?|(?:\d\.\d+)?')

# Exercice 4 Trouver l'erreur :
# A)
def line(a, b):
    def f(x):
        return a * x + b
    return f

# B)
def count(n):
    if n == 0:
        return 0
    if n%2 == 0:
        return 1+count(n/2)
    return 1+count((n-1)/2)

# Exercice 5 Filtrage de listes :
def even(x):
    return x%2 == 0
        
def lower(a):
    def minor(x):
        return x < a
    return minor

def filer(data, condition):
    result = []
    for elem in data:
        if condition(elem):
            result.append(elem)
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(data, even))
print(filter(data, lower(3)))
print(filter(data, lower(5)))