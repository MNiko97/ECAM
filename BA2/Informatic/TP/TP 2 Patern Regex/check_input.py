import re

contact='''
+32 484 73 42 51
32 498 56 56 32
+32 497 79 97 98
32 485 52 25 56 6
0484 75 96 63
484 5 89 96
'''

plate='''
2RTY558
4575UIY
3265556
7896IUYH
'''
number_int = '''
+4564
456
-445
d99zadzdze
56f6
+ 56
 8 6
     9
++89
8+9
 -99
    + 55
'''
test_path='''
szsazA:\\
5:\\ 
g:\\
B.\\
C.\
D:\
E::\\
F:\\\
AZ:\\

T:\\
T:\\\
T::\\
'''
def check_phone ():
    pattern = re.compile(r'\+\d\d\s\d\d\d\s\d\d\s\d\d\s\d\d')
    phone_number = pattern.finditer(contact)
    for item in phone_number :
        print(item)
    
def check_plate():
    pattern_1 = re.compile(r'\d[A-Z][A-Z][A-Z]\d\d\d')
    pattern_2 = re.compile(r'\d\d\d\d[A-Z][A-Z][A-Z]')
    valid_1 = pattern_1.finditer(plate)
    valid_2 = pattern_2.finditer(plate)
    for item in valid_1 :
        print(item)
    for item in valid_2 :
        print(item)

def check_int():
    pattern_1 = re.findall(r'[+-][0-9]+', number_int)
    #pattern_2 = re.findall(r'\S[0-9]+', number_int)
    for item in pattern_1 :
        print(item)
   
def check_path():
    path = input('Type your path : ')
    pattern = re.finditer(r'^[A-Z]{1}(:\\){1}', path)
    if pattern :
        print("True")
    
def search_number():
    pass

def url_cut():
    pass

check_phone()