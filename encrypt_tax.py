# Simple encryption for salary

def encrypt(salary, key):
    return salary + key

def decrypt(enc_salary, key):
    return enc_salary - key

# Example
salary = 50000
key = 1234  # secret encryption key

# Encrypt salary
enc_salary = encrypt(salary, key)

# Calculate 10% tax on encrypted salary
enc_tax = enc_salary * 0.10

# Decrypt tax
tax = decrypt(enc_tax, key * 0.10)

print(f"Original salary: {salary}")
print(f"Encrypted salary: {enc_salary}")
print(f"Tax on salary (after decrypting): {tax}")
