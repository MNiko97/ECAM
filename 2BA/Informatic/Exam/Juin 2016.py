# Exercice 3 Expression régulière :
import re

postalPattern = re.compile(r'[1-9]\d{3,4}')
wordPattern = re.compile(r'(\w+)\s\1')
pricePattern = re.compile(r'([1-9]\d+)|([1-9]\d+[.]\d+)|\d|\d{1}[.]\d+')

#Exercice 4 Trouver l'erreur :
# A)
pattern = '[A-Z]:(\\\\[^<>:"/\|?*]+)*'
p = re.compile(pattern)

print(p.match("C:\\Users\\lur\\Desktop"))
print(p.match("/home/usr/Desktop"))

# B) 
from turtle import *
def vonkoch(dist):
    if dist <= 5:
        forward(dist)
    else:
        vonkoch(dist/3)
        left(60)
        vonkoch(dist/3)
        left(120)
        vonkoch(dist/3)
        left(60)
        vonkoch(dist/3)

'''vonkoch(200)
done()'''

# Exercice 5 Multiplier des matrices :
def transpose(matrix):
    trans = []
    for j in range(len(matrix[0])):
        trans.append([])
        for i in range(len(matrix)):
            trans[j].append(matrix[i][j])
    return trans

def getRowMultiplier(row):
    def multiplier(col):
        res = 0
        for i in range(len(row)):
            res += row[i] * col[i]
        return res
    return multiplier


def multiply(A, B):
    if len(A[0]) != len(B):
        raise ArithmeticError("Incompatible Matrix sizes")
    res = []
    columnsOfB = transpose(B)
    for row in A:
        res.append(list(map(getRowMultiplier(row), columnsOfB)))
    return res

matrix = [
    [1, 2],
    [3, 4]
]
print(multiply(matrix, matrix))