# Simple additive "encryption" (for demo)

def encrypt(num, key):
    return num + key

def decrypt(enc_num, key):
    return enc_num - key

# Example
key = 50  # secret key
a = 20
b = 30

enc_a = encrypt(a, key)
enc_b = encrypt(b, key)

# Add encrypted numbers
enc_sum = enc_a + enc_b

# Decrypt the result
sum_result = decrypt(enc_sum, key * 2)

print(f"Original numbers: {a} and {b}")
print(f"Encrypted numbers: {enc_a} and {enc_b}")
print(f"Decrypted sum: {sum_result}")
