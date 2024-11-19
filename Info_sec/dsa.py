import hashlib
import random

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys(p, q, g):
    x = random.randint(1, q - 1)  # Private key
    y = pow(g, x, p)             # Public key
    return (x, y)

def sign(message, p, q, g, x):
    k = random.randint(1, q - 1)
    r = pow(g, k, p) % q
    k_inv = mod_inverse(k, q)
    hash_value = int(hashlib.sha1(message.encode()).hexdigest(), 16)
    s = (k_inv * (hash_value + x * r)) % q
    return (r, s)

def verify(message, signature, p, q, g, y):
    r, s = signature
    if not (0 < r < q and 0 < s < q):
        return False
    w = mod_inverse(s, q)
    hash_value = int(hashlib.sha1(message.encode()).hexdigest(), 16)
    u1 = (hash_value * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

# Example usage
p = 23  # A large prime (for simplicity, smaller values are used here)
q = 11  # A divisor of p-1
g = 2   # g < p

# Generate keys
private_key, public_key = generate_keys(p, q, g)
message = "HELLO"

# Sign the message
signature = sign(message, p, q, g, private_key)
print("Signature:", signature)

# Verify the signature
is_valid = verify(message, signature, p, q, g, public_key)
print("Signature valid:", is_valid)
