# Juin 2017

# Exercie 2 Theorie :
def fun():
    def f(a,b):
        return a + b
    return f

v = fun()
result = v(12, -2)
print(result)

# Exercice 3 Expression régulière :
import re

notePattern = re.compile('(\d{1,2}|\d{1,2}[.]\d{1,2})(/100)')
platePattern = re.compile('([A-Z]{3}[1-9]{3})|([1-9]{3}[A-Z]{3})')
gatePattern = re.compile('([A]|[B])[1-9]{1,2}')

'''wordInput = input("Write a pattern to check : ")
valid = notePattern.match(wordInput)
valid1 = platePattern.match(wordInput)
valid2 = gatePattern.match(wordInput)

if valid or valid1 or valid2:
    print(True)
else:
    print(False)'''

# Exercice 4 Trouver l'erreur :
# A)
def fact(n):
    result = 1
    if n > 0 :
        prev = fact(n-1)
        result = n * prev
    return result

# B)
def price(items):
    result = []
    pattern = re.compile(r'P=\d+', re.MULTILINE)
    for m in pattern.finditer(items):
        result.append(int(m.group(0).replace('P=','')))
    return result

#print(price('''C=182738;P=12;Q=2;S=29.C=273616;P=24;Q=7;S=11.'''))

# Exercice 5 Compléter le code :
# A)
def log(f):
    def wrapper(*args):
        print(" Args :", args)
        print("Result :", f(*args))
        return f(*args)
    return wrapper

@log
def add(a, b):
    return a+b

#print(add(2,9))

# B)
import time, threading
def warn(t, msg):
    def do():
        time.sleep(t)
        print(msg)
    threading.Thread(target=do).start()

warn(2, 'COUCOU !')
for i in range(5):
    print(i)
    time.sleep(1)
