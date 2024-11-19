def columnar_encrypt(plaintext, key):
    # Remove spaces from the plaintext and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    
    # Calculate the number of columns
    key_length = len(key)
    num_rows = len(plaintext) // key_length + (1 if len(plaintext) % key_length else 0)

    # Create a grid to hold the plaintext characters
    grid = [''] * num_rows

    # Fill the grid with plaintext characters
    for i in range(len(plaintext)):
        row = i // key_length
        col = i % key_length
        grid[row] += plaintext[i]

    # Create a list of tuples (column_index, column_data) based on the key
    columns = sorted((key[i], i) for i in range(key_length))
    
    # Read the columns in the order defined by the sorted key
    ciphertext = ''
    for _, col_index in columns:
        for row in grid:
            if col_index < len(row):
                ciphertext += row[col_index]

    return ciphertext

def columnar_decrypt(ciphertext, key):
    # Calculate the number of columns and rows
    key_length = len(key)
    num_rows = len(ciphertext) // key_length + (1 if len(ciphertext) % key_length else 0)

    # Create a grid to hold the ciphertext characters
    grid = [''] * num_rows

    # Create a list of tuples (column_index, column_data) based on the key
    columns = sorted((key[i], i) for i in range(key_length))

    # Calculate the number of characters in each column
    column_lengths = [num_rows] * key_length
    for i in range(len(ciphertext) % key_length):
        column_lengths[i] -= 1

    # Fill the grid with the ciphertext characters based on the sorted key
    index = 0
    for _, col_index in columns:
        for row in range(column_lengths[col_index]):
            grid[row] += ciphertext[index]
            index += 1

    # Read the plaintext from the grid row by row
    plaintext = ''
    for row in grid:
        plaintext += row

    return plaintext

# Example usage
if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    key = "KEY"

    encrypted = columnar_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")

    decrypted = columnar_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")