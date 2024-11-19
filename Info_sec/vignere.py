def vigenere_cipher(text, key, mode='encrypt'):
    key = key.upper()
    text = text.replace(" ", "").upper()
    key_repeated = (key * ((len(text) // len(key)) + 1))[:len(text)]
    result = []

    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key_repeated[i]) - ord('A')
            if mode == 'encrypt':
                result.append(chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A')))
            elif mode == 'decrypt':
                result.append(chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A')))
        else:
            result.append(text[i])

    return ''.join(result)

# Example usage
text = "HELLO WORLD"
key = "KEY"
encrypted = vigenere_cipher(text, key, mode='encrypt')
print("Encrypted Text:", encrypted)
decrypted = vigenere_cipher(encrypted, key, mode='decrypt')
print("Decrypted Text:", decrypted)
