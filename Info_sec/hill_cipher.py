import numpy as np

def mod26(matrix):
    """Applies modulo 26 to all elements of the matrix."""
    return matrix % 26

def get_inverse(matrix):
    """Calculates the inverse of a matrix modulo 26."""
    det = int(np.round(np.linalg.det(matrix)))  # Determinant
    det_inv = pow(det, -1, 26)  # Modular inverse of the determinant
    
    # Adjugate matrix
    matrix_mod = mod26(matrix)
    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    return mod26(matrix_inv)

def prepare_text(text):
    """Prepares text by removing spaces and converting to uppercase."""
    return ''.join(text.split()).upper()

def encrypt(plaintext, key_matrix):
    plaintext = prepare_text(plaintext)
    n = key_matrix.shape[0]
    
    # Pad the plaintext if necessary
    while len(plaintext) % n != 0:
        plaintext += 'X'  # Padding character

    ciphertext = []
    
    for i in range(0, len(plaintext), n):
        block = [ord(char) - ord('A') for char in plaintext[i:i+n]]
        block_matrix = np.array(block).reshape(n, 1)
        encrypted_block = mod26(np.dot(key_matrix, block_matrix))
        ciphertext.extend(encrypted_block.flatten().astype(int))

    return ''.join(chr(c + ord('A')) for c in ciphertext)

def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    key_matrix_inv = get_inverse(key_matrix)
    
    plaintext = []
    
    for i in range(0, len(ciphertext), n):
        block = [ord(char) - ord('A') for char in ciphertext[i:i+n]]
        block_matrix = np.array(block).reshape(n, 1)
        decrypted_block = mod26(np.dot(key_matrix_inv, block_matrix))
        plaintext.extend(decrypted_block.flatten().astype(int))

    return ''.join(chr(p + ord('A')) for p in plaintext)

# Example usage
if __name__ == "__main__":
    plaintext = "HELLO"
    key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix

    encrypted = encrypt(plaintext, key_matrix)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt(encrypted, key_matrix)
    print(f"Decrypted: {decrypted}")