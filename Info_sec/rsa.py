import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    """Generate a random prime number of specified bit length."""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1  # Ensure p is of specified length and odd
    return p

def generate_prime_number(length):
    """Generate a prime number of specified bit length."""
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keypair(length):
    """Generate a public/private key pair."""
    p = generate_prime_number(length)
    q = generate_prime_number(length)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e
    e = 65537  # Common choice for e
    
    # Compute d
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))  # Public and private keys

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    e, n = public_key
    plaintext_int = int.from_bytes(plaintext.encode(), 'big')
    ciphertext = pow(plaintext_int, e, n)
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using the private key."""
    d, n = private_key
    plaintext_int = pow(ciphertext, d, n)
    # Convert back to bytes
    plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big')
    return plaintext_bytes.decode()

# Example usage
if __name__ == "__main__":
    # Generate a keypair
    public_key, private_key = generate_keypair(8)  # Use 8 bits for simplicity; use larger for real applications

    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")

    # Message to encrypt
    message = "HELLO"
    print(f"Original message: {message}")

    # Encrypt the message
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")