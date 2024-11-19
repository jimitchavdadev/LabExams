def railfence_encrypt(plaintext, rails):
    # Create a 2D list (list of lists) for the rails
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    
    direction_down = False
    row, col = 0, 0

    # Fill the fence with characters in a zigzag pattern
    for char in plaintext:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down  # Change direction at the top or bottom rail
        fence[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    # Read the fence row by row to create the ciphertext
    ciphertext = ''.join([''.join(row) for row in fence]).replace('\0', '')
    return ciphertext

def railfence_decrypt(ciphertext, rails):
    # Create a 2D list to hold the characters
    fence = [['\0' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    direction_down = None
    row, col = 0, 0

    # Mark the positions in the fence where characters will go
    for char in ciphertext:
        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        
        fence[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Fill the fence with the ciphertext
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*' and index < len(ciphertext):
                fence[i][j] = ciphertext[index]
                index += 1

    # Read the characters from the fence in a zigzag pattern to decrypt
    plaintext = ''
    row, col = 0, 0
    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        
        if fence[row][col] != '\0':
            plaintext += fence[row][col]
            col += 1
            row += 1 if direction_down else -1
        else:
            col += 1  # Move to the next column if current position is empty

    return plaintext

# Example usage
if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    rails = 3

    encrypted = railfence_encrypt(plaintext, rails)
    print(f"Encrypted: {encrypted}")

    decrypted = railfence_decrypt(encrypted, rails)
    print(f"Decrypted: {decrypted}")