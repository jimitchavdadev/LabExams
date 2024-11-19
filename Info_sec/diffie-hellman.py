import random

# Function to compute base^exp % mod
def power_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Function to generate a Diffie-Hellman public key
def generate_public_key(p, g, private_key):
    return power_mod(g, private_key, p)

# Function to compute the shared secret key
def compute_shared_secret(public_key, private_key, p):
    return power_mod(public_key, private_key, p)

# Example usage
# Alice and Bob agree on a large prime p and a base g
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Alice and Bob each select a private key
alice_private = random.randint(1, p-1)
bob_private = random.randint(1, p-1)

# Alice and Bob compute their public keys
alice_public = generate_public_key(p, g, alice_private)
bob_public = generate_public_key(p, g, bob_private)

# Alice and Bob exchange public keys, then compute the shared secret
alice_shared_secret = compute_shared_secret(bob_public, alice_private, p)
bob_shared_secret = compute_shared_secret(alice_public, bob_private, p)

print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)
print("Alice's Shared Secret:", alice_shared_secret)
print("Bob's Shared Secret:", bob_shared_secret)

# Verify the shared secret is the same
assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
