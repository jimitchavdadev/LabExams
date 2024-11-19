def create_playfair_matrix(keyword):
    # Prepare the keyword by removing duplicates and converting to uppercase
    keyword = ''.join(sorted(set(keyword), key=keyword.index)).upper()
    
    # Create a 5x5 matrix and fill it with the keyword letters
    matrix = []
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' is omitted
    for char in keyword:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]  # Create 5x5 matrix

def format_text(text):
    text = text.upper().replace('J', 'I')  # Replace J with I
    formatted_text = ''
    
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:  # If the same letter occurs, insert 'X'
                formatted_text += text[i] + 'X'
                i += 1
            else:
                formatted_text += text[i] + text[i + 1]
                i += 2
        else:
            formatted_text += text[i] + 'X'  # If odd length, append 'X'
            i += 1
            
    return formatted_text

def find_position(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_encrypt(plaintext, keyword):
    matrix = create_playfair_matrix(keyword)
    formatted_text = format_text(plaintext)
    ciphertext = ''
    
    for i in range(0, len(formatted_text), 2):
        a, b = formatted_text[i], formatted_text[i + 1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)
        
        if row_a == row_b:  # Same row
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:  # Same column
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:  # Rectangle
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]
    
    return ciphertext

def playfair_decrypt(ciphertext, keyword):
    matrix = create_playfair_matrix(keyword)
    formatted_text = ciphertext
    plaintext = ''
    
    for i in range(0, len(formatted_text), 2):
        a, b = formatted_text[i], formatted_text[i + 1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)
        
        if row_a == row_b:  # Same row
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:  # Same column
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        else:  # Rectangle
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]
    
    return plaintext

# Example usage
if __name__ == "__main__":
    keyword = "KEYWORD"
    plaintext = "HELLO WORLD"
    
    encrypted = playfair_encrypt(plaintext, keyword)
    print(f"Encrypted: {encrypted}")
    
    decrypted = playfair_decrypt(encrypted, keyword)
    print(f"Decrypted: {decrypted}")