# Python RSA Encryption

A from-scratch implementation of the RSA public-key cryptosystem in Python, built to understand the number theory behind asymmetric encryption rather than relying on an existing crypto library.

## How it works

RSA encryption relies on the fact that multiplying two large prime numbers is easy, but factoring their product back into the original primes is computationally hard. This program implements that process step by step:

1. **Key generation** — the user supplies two prime numbers, `p1` and `p2`. The program computes:
   - `N = p1 * p2` (the modulus, shared publicly)
   - `Z = (p1 - 1) * (p2 - 1)` (Euler's totient of N)
2. **Choosing the public exponent `e`** — `e` must be coprime with `Z`. The program checks this using the Euclidean algorithm (`gcd`), and lets the user either supply their own `e` or generate one at random.
3. **Deriving the private exponent `d`** — the program solves `d * e ≡ 1 (mod Z)` by searching for an integer solution to `d = (1 + x*Z) / e`.
4. **Encryption** — each character of the message is converted to its ASCII value, then encrypted using modular exponentiation: `ciphertext = (ascii_value ^ e) mod N`.

## Example

Enter YOUR prime number: 61
Enter the OTHER PERSON'S prime number: 53
What message would you like to encode? hi
...
Encrypted message: ['1855', '2494']
Encryption Key: 17
Decryption Key: 2753
Product of Primes: 3233

## Why I built this

I wanted to actually understand the math behind public-key cryptography, modular exponentiation, coprimality, and modular inverses, by implementing it myself instead of importing a library and treating it as a black box.

## Built with

Python 3, standard library only (`random`) — no external cryptography packages.

