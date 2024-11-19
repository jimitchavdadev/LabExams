import numpy as np

def hill_cipher(text, key_matrix, mode='encrypt'):
    text = text.replace(" ", "").upper()
    n = len(key_matrix)
    text = text + "X" * (n - len(text) % n) if len(text) % n != 0 else text
    text_vectors = [np.array([ord(char) - ord('A') for char in text[i:i + n]]) for i in range(0, len(text), n)]

    if mode == 'decrypt':
        det = int(round(np.linalg.det(key_matrix)))
        det_inv = pow(det, -1, 26)
        adjugate_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
        key_matrix = (det_inv * adjugate_matrix) % 26

    result = []
    for vector in text_vectors:
        encrypted_vector = np.dot(key_matrix, vector) % 26
        result.extend([chr(num + ord('A')) for num in encrypted_vector])

    return ''.join(result)

# Example usage
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
text = "HELLO"
encrypted = hill_cipher(text, key_matrix, mode='encrypt')
print("Encrypted Text:", encrypted)
decrypted = hill_cipher(encrypted, key_matrix, mode='decrypt')
print("Decrypted Text:", decrypted)
