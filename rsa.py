#Key Generation
#First, we need to generate the RSA keys (public and private). 
#This involves selecting two large prime numbers, calculating their product, 
#and then finding the public and private exponents.
import random
import math


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Function to generate a random prime number
def generate_prime():
    while True:
        prime = random.randint(2 ** 16, 2 ** 32)
        if is_prime(prime):
            return prime

# Function to generate RSA key pair
def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    print(f'First Prime Number: {p}')
    print(f'The second Prime Number: {q}')
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, phi)
        print(e)
        if math.gcd(e, phi) == 1:
            break
    d = pow(e, -1, phi)
    return ((n, e), (n, d))

# Generate keys
public_key, private_key = generate_keypair()
print("Public Key:", public_key)
print("Private Key:", private_key)



#Encryption
#Next, we use the public key to encrypt a message. 
#The message is converted to an integer and then encrypted using the public exponent and modulus.

# Function to encrypt a message
def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Encrypt a message
message = input('Please write the message to be encrypted: ')
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)



#DECRYPTION
#Finally, we use the private key to decrypt the message. 
#The encrypted integers are converted back to characters using the private exponent and modulus.

# Function to decrypt a message
def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Decrypt the message
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)


#Explanation
# 1.Key Generation: We generate two large prime numbers ( p ) and ( q ), calculate their product ( n ), and compute the totient ( \phi(n) ). 
# We then choose a public exponent ( e ) that is coprime with ( \phi(n) ) and calculate the private exponent ( d ) as the modular inverse of ( e ) modulo ( \phi(n) ).

# 2.Encryption: The message is converted to an integer and encrypted using the formula ( c = m^e \mod n ), where ( m ) is the message, ( e ) is the public exponent, and ( n ) is the modulus.

# 3.Decryption: The encrypted message is decrypted using the formula ( m = c^d \mod n ), where ( c ) is the encrypted message, ( d ) is the private exponent, and ( n ) is the modulus.

#This example demonstrates the basic principles of RSA encryption and decryption. If you have any questions or need further clarification, feel free to ask!