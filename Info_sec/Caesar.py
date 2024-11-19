def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Handle shifts larger than 26
            # Determine the ASCII offset based on case
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are unchanged
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decrypting is just encrypting with the negative shift

# Example usage
if __name__ == "__main__":
    plaintext = "Hello, World!"
    shift = 3

    encrypted = caesar_encrypt(plaintext, shift)
    print(f"Encrypted: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")