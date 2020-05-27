'''
Mission 2: RSA Encryption
Author: Mitrovic Nikola
Version: April 10, 2020
'''
import numpy as np 
import random as r

def isPrime(n):                                 
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True

def isCoPrime(a, b): 
    greatCommonDivisor = lambda a, b: a if not b else greatCommonDivisor(b, a%b)    # Return the value of the greatest common divisor
    if (greatCommonDivisor(a, b) == 1):                                             # Definition of coprime number
        return True
    else:
        return False

def generatePrimeNumber(bitSize):               
    n = r.getrandbits(bitSize)                  # Generate random bitsized number
    while not isPrime(n):
        n = r.getrandbits(bitSize)
    return n

def generatePublicKey(bitSize): 
    p = generatePrimeNumber(int(bitSize/2))
    q = generatePrimeNumber(int(bitSize/2))
    n = p*q
    phi = (p-1)*(q-1)
    e = r.randint(1, phi)
    while not isCoPrime(e, phi) or not isCoPrime(e, n):         # In RSA encryption e has to be coprime with phi and n
        e = r.randint(1, phi)
    return (e, n), phi

def generatePrivateKey(publicKey, phi):
    e, n = publicKey
    array = np.array([[phi, e], [phi, 1]]) 
    while array[0, 1] != 1 :                                    # To find d we have to resolve this equation : e^d mod(phi) = 1
        divider = int(array[0, 0]/array[0, 1])
        a = array[:, 1]*divider
        b = array[:, 0] - a
        if b[1] < 0 :
            b[1] = b[1]%phi
        array[:, 0] = array[:, 1]
        array[:, 1] = b
    d = int(array[1,1])
    return (d, n)

def encrypt(publicKey, msg):
    e, n = publicKey
    cipheredMessage = [(ord(letter) ** e) % n for letter in msg]     
    decodedMessage = [chr(byteLetter) for byteLetter in cipheredMessage]       # ord() encode every letter in the message with utf8 then cipher with the formula (msg^e)mod(n)        
    return cipheredMessage, decodedMessage

def decrypt(privateKey, cipheredMessage):
    d, n = privateKey
    decryptedMessage = [chr((char ** d) % n) for char in cipheredMessage]       # char() decode very byte into actual character with utf8 then decipher with the formula (msg^d)mod(n)
    return decryptedMessage

def main(bits):
    print("__________STARTING RSA ENCRYPTION SCRIPT__________")
    msg = str(input("Write your message : "))
    print("\nGenerating Public and Private Key ...")
    publicKey, phi = generatePublicKey(bits)
    privateKey = generatePrivateKey(publicKey, phi)
    print("Public Key : ", publicKey, "\nPrivate Key : ", privateKey)
    encrypted_msg, decoded_encrypted_msg = encrypt(publicKey, msg)
    print("\nEncrypted Message : ")
    print(''.join(map(lambda x: str(x), encrypted_msg))," or decoded in UTF8 :  ", ''.join(map(lambda x: str(x), decoded_encrypted_msg)), )
    print("\nDecrypted Message : ")
    print(''.join(map(lambda x: str(x), decrypt(privateKey, encrypted_msg))))
    print("\n__________ENDING OF RSA ENCRYPTION SCRIPT__________")

main(16)