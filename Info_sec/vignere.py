def vigenere_encrypt(plaintext, keyword):
    encrypted_text = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():  # Only encrypt alphabetic characters
            # Calculate the shift
            shift = ord(k.upper()) - ord('A')
            # Encrypt the character
            encrypted_char = chr((ord(p.upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(p)  # Non-alphabetic characters are unchanged

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():  # Only decrypt alphabetic characters
            # Calculate the shift
            shift = ord(k.upper()) - ord('A')
            # Decrypt the character
            decrypted_char = chr((ord(c.upper()) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(c)  # Non-alphabetic characters are unchanged

    return ''.join(decrypted_text)


# Example usage
if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    keyword = "KEY"

    encrypted = vigenere_encrypt(plaintext, keyword)
    print(f"Encrypted: {encrypted}")

    decrypted = vigenere_decrypt(encrypted, keyword)
    print(f"Decrypted: {decrypted}")