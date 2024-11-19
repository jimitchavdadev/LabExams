import hashlib
import random

def generate_parameters(q_length=160, p_length=1024):
    """Generate DSA parameters p, q, and g."""
    # Generate a prime q of length q_length
    q = random.getrandbits(q_length)
    while not is_prime(q):
        q = random.getrandbits(q_length)

    # Generate a prime p of length p_length such that p-1 is divisible by q
    p = generate_large_prime(p_length, q)
    
    # Generate g
    g = pow(2, (p - 1) // q, p)
    
    return p, q, g

def is_prime(n, k=128):
    """Check if n is a prime number using Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find d such that n = 2^r * d + 1 for some r >= 1
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(length, q):
    """Generate a large prime p such that (p-1) is divisible by q."""
    p = random.getrandbits(length)
    while not is_prime(p) or (p - 1) % q != 0:
        p = random.getrandbits(length)
    return p

def dsa_sign(message, p, q, g, x):
    """Sign a message using DSA."""
    # Hash the message
    H = int(hashlib.sha256(message.encode()).hexdigest(), 16)

    # Choose a random k
    k = random.randint(1, q - 1)

    # Compute r
    r = pow(g, k, p) % q

    # Compute s
    k_inv = pow(k, -1, q)
    s = (k_inv * (H + x * r)) % q

    return r, s

def dsa_verify(message , p, q, g, y, r, s):
    """Verify a DSA signature."""
    # Hash the message
    H = int(hashlib.sha256(message.encode()).hexdigest(), 16)

    # Check if r and s are in the valid range
    if not (0 < r < q and 0 < s < q):
        return False

    # Compute w
    w = pow(s, -1, q)

    # Compute u1 and u2
    u1 = (H * w) % q
    u2 = (r * w) % q

    # Compute v
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q

    # The signature is valid if v == r
    return v == r

# Example usage
if __name__ == "__main__":
    # Generate DSA parameters
    p, q, g = generate_parameters()

    # Choose a private key x
    x = random.randint(1, q - 1)

    # Compute the public key y
    y = pow(g, x, p)

    # Message to sign
    message = "HELLO DSA"
    print(f"Original message: {message}")

    # Sign the message
    r, s = dsa_sign(message, p, q, g, x)
    print(f"Signature: (r={r}, s={s})")

    # Verify the signature
    is_valid = dsa_verify(message, p, q, g, y, r, s)
    print(f"Signature valid: {is_valid}")