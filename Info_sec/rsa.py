import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 0:
            return d
    return None

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be the same.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    return [(ord(char) ** e) % n for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr((char ** d) % n) for char in ciphertext])

# Example usage
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
message = "HELLO"
encrypted = encrypt(public_key, message)
print("Encrypted:", encrypted)
decrypted = decrypt(private_key, encrypted)
print("Decrypted:", decrypted)
