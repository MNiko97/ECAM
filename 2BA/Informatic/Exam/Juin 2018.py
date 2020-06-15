# Examen Juin 2018

# Exercice 1.1 Programmation fonctionnelle :
from functools import reduce
def reduce(fn, L, init):
    acc = init
    for elem in L:
        fc = fn
        acc = fc(elem, acc)
    return acc
    
def limitMax(maximum):
    def limit(elem, acc):
        if elem <= maximum:
            acc.append(elem)
        else:
            acc.append(maximum)
        return acc
    return limit

print(reduce(limitMax(3), [1, 2, 3, 4, 5, 6], []))

# Exercice 1.2 Fonction Récursive :
from math import sin
def zero(fn, inf, sup):
    m = (inf + sup)/2
    if fn(m) == 0 or sup-inf > 0.000001:
        return m
    elif fn(inf) * fn(sup) < 0 :
        return zero(fn, inf, m)
    elif fn(inf) * fn(sup) > 0 :
        return zero(fn, m, sup)
    else:
        return None

# Exercice 1.3 Décorateur :
def password(pswd):
    def decorator(func):
        def wrapper(*args):
            if len(args) == 3 :
                word, a, b = args
                if word == pswd:
                    return func(a, b)
                raise ValueError
            raise ValueError
        return wrapper
    return decorator

@password("secret")
def add(a, b):
    return a+b

'''add("hacker", 1, 2)
add(1, 2)
add("secret", 1, 2)'''

# Exercice 1.4 Arbres :
import copy 
class Tree:
    def __init__(self, value, left=None, right=None, children=()):
        self.value = value
        self.left = left
        self.right = right
        self.__children = children
    
    @property
    def value(self):
        return self.value


def treeMax(tree):
    for branch in tree :
        print(branch)

t = Tree(0, Tree(4, Tree(-5), Tree(3, Tree(8), Tree(1))), Tree(2, Tree(4)))
a = Tree(4)
