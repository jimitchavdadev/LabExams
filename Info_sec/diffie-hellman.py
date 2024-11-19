import random

def generate_prime_candidate(length):
    """Generate a random prime number of specified bit length."""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1  # Ensure p is of specified length and odd
    return p

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

def generate_large_prime(length):
    """Generate a large prime number."""
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def diffie_hellman():
    # Generate a large prime number p and a base g
    p = generate_large_prime(512)  # Use a larger bit length for real applications
    g = 2  # Common choice for g

    # Alice's private key
    a = random.randint(1, p - 1)
    # Alice's public key
    A = pow(g, a, p)

    # Bob's private key
    b = random.randint(1, p - 1)
    # Bob's public key
    B = pow(g, b, p)

    # Exchange public keys and compute shared secret
    # Alice computes the shared secret
    shared_secret_Alice = pow(B, a, p)
    # Bob computes the shared secret
    shared_secret_Bob = pow(A, b, p)

    return p, g, A, B, shared_secret_Alice, shared_secret_Bob

# Example usage
if __name__ == "__main__":
    p, g, A, B, shared_secret_Alice, shared_secret_Bob = diffie_hellman()
    print(f"Prime p: {p}")
    print(f"Base g: {g}")
    print(f"Alice's Public Key A: {A}")
    print(f"Bob's Public Key B: {B}")
    print(f"Alice's Shared Secret: {shared_secret_Alice}")
    print(f"Bob's Shared Secret: {shared_secret_Bob}")