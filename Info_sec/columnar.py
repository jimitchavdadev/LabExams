def columnar_cipher(text, key, mode='encrypt'):
    key_order = sorted((char, idx) for idx, char in enumerate(key))
    key_indices = [idx for _, idx in key_order]
    text = text.replace(" ", "").upper()

    if mode == 'encrypt':
        rows = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
        if len(rows[-1]) < len(key):
            rows[-1] += "X" * (len(key) - len(rows[-1]))
        columns = ["".join(row[idx] for row in rows) for idx in key_indices]
        return "".join(columns)

    elif mode == 'decrypt':
        num_rows = len(text) // len(key)
        extra = len(text) % len(key)
        col_lengths = [num_rows + (1 if i < extra else 0) for i in range(len(key))]
        columns = []
        start = 0
        for length in col_lengths:
            columns.append(text[start:start+length])
            start += length
        rows = ["".join(columns[key_indices.index(i)][row] if row < len(columns[key_indices.index(i)]) else "" for i in range(len(key))) for row in range(num_rows)]
        return "".join(rows)

# Example usage
text = "HELLO WORLD"
key = "KEYWORD"
encrypted = columnar_cipher(text, key, mode='encrypt')
print("Encrypted Text:", encrypted)
decrypted = columnar_cipher(encrypted, key, mode='decrypt')
print("Decrypted Text:", decrypted)
