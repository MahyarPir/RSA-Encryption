
"""
Python RSA Encryption by Mahyar Pirayesh
"""
import random


def encrypt_with_ascii():
    print("Python RSA Encryption by Mahyar Pirayesh")
    # The following defines a library with all letters in association to their number and binary according to ASCII
    asciiDict = {chr(i): i for i in range(128)}

    p1 = int(input("Enter YOUR prime numer: "))
    p2 = int(input("Enter the OTHER PERSON'S prime numer: "))
    message = input("What message would you like to encode? ")

    # N is the product of the primes
    N = p1 * p2

    # Z is the product of one less than each prime
    Z = (p1 - 1) * (p2 - 1)

    # Code for checking if two numbers are co-prime
    def gcd(p, q):
        while q != 0:
            p, q = q, p % q
        return p

    def is_coprime(x, y):
        return gcd(x, y) == 1  # Returns True or False

    # We select an "e" such that e is coprime with Z. This is necessary to the encryption process
    # Option 1: manually entered e
    if int(input(
            "Would you like to manually enter an encryption key or have it be made randomly? Enter 1 to manually input \"e\" and enter 2 for a randomly generated \"e\": ")) == 1:
        while True:
            e = int(input(
                f"What would you like the encryption key to be? \"e\" needs to be co-prime with Z: {Z} and no more than {Z}: "))
            if is_coprime(e, Z) and e > 0 and e < (Z):
                break
                # Option 2: random e
    else:
        while True:
            e = random.randint(2, Z - 1)  # 1 < e < Z ; gcf(e, Z) = 1
            if is_coprime(e, Z):
                break

    # We find an integer d with this while loop --- d = Decryption Key --- d*e ≡ 1(mod Z)
    for x in range(1, 1000000000000):
        d = (1 + x * Z) / e
        if d.is_integer():
            break

    encrypted_list = []
    for letter in message:
        encrypted_list.append(str(((asciiDict[letter]) ** e) % N))
    return ("Encrypted message: " + str(encrypted_list), "Encryption Key: " + str(e), "Decryption Key: " + str(d),
            "Product of Primes: " + str(N),
            "Side Note: Only share the product of the primes, the encryption key, and the message with your recipient!")


print(encrypt_with_ascii())
