def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

# Example
n = 10
print(f"Euler's Totient Function φ({n}) = {euler_totient(n)}")
