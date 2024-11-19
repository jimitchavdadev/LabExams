def generate_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is typically excluded
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates, replace 'J' with 'I'
    key += "".join([ch for ch in alphabet if ch not in key])  # Fill with remaining letters
    return [key[i:i+5] for i in range(0, 25, 5)]


def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:  # Add 'X' if letters repeat in a pair
            result += "X"
        elif i + 1 < len(text):
            result += text[i + 1]
        i += 2
    if len(result) % 2 != 0:
        result += "X"  # Add 'X' to make even length
    return result


def find_position(matrix, letter):
    for row, line in enumerate(matrix):
        if letter in line:
            return row, line.index(letter)
    return None


def playfair_cipher(text, key, mode="encrypt"):
    matrix = generate_key_matrix(key)
    text = preprocess_text(text)
    shift = 1 if mode == "encrypt" else -1
    result = ""
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # Same row
            result += matrix[row_a][(col_a + shift) % 5]
            result += matrix[row_b][(col_b + shift) % 5]
        elif col_a == col_b:  # Same column
            result += matrix[(row_a + shift) % 5][col_a]
            result += matrix[(row_b + shift) % 5][col_b]
        else:  # Rectangle swap
            result += matrix[row_a][col_b]
            result += matrix[row_b][col_a]

    return result


# Example usage
key_phrase = "Playfair Example"
plain_text = "Hide the gold in the tree stump"
cipher_text = playfair_cipher(plain_text, key_phrase, mode="encrypt")
print("Encrypted Text:", cipher_text)

decrypted_text = playfair_cipher(cipher_text, key_phrase, mode="decrypt")
print("Decrypted Text:", decrypted_text)
