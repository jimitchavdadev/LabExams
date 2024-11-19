def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around within the alphabet
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result

# Example usage
plain_text = "Hello, World!"
shift_amount = 3

# Encrypt
encrypted_text = caesar_cipher(plain_text, shift_amount, mode='encrypt')
print("Encrypted Text:", encrypted_text)

# Decrypt
decrypted_text = caesar_cipher(encrypted_text, shift_amount, mode='decrypt')
print("Decrypted Text:", decrypted_text)
