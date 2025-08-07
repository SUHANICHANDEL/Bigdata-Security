import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p * q
    phi = (p-1)*(q-1)

    e = random.randrange(1, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

# Example
p = 17
q = 19
public, private = generate_keypair(p, q)
print(f"Public key: {public}")
print(f"Private key: {private}")

message = "Hi"
encrypted_msg = encrypt(public, message)
print(f"Encrypted message: {encrypted_msg}")

decrypted_msg = decrypt(private, encrypted_msg)
print(f"Decrypted message: {decrypted_msg}")
