def rail_fence_cipher(text, key, mode='encrypt'):
    text = text.replace(" ", "").upper()
    rails = [[] for _ in range(key)]
    if mode == 'encrypt':
        row, direction = 0, 1
        for char in text:
            rails[row].append(char)
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        return ''.join(''.join(rail) for rail in rails)
    elif mode == 'decrypt':
        indices = [0] * len(text)
        row, direction, idx = 0, 1, 0
        for i in range(len(text)):
            indices[i] = row
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        sorted_indices = sorted(range(len(indices)), key=lambda i: indices[i])
        for i, char in zip(sorted_indices, text):
            indices[i] = char
        return ''.join(indices)

# Example usage
text = "HELLO WORLD"
key = 3
encrypted = rail_fence_cipher(text, key, mode='encrypt')
print("Encrypted Text:", encrypted)
decrypted = rail_fence_cipher(encrypted, key, mode='decrypt')
print("Decrypted Text:", decrypted)
