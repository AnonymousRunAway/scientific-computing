def vigenere(query: str, key: str, decrypt: bool = False) -> str:
    query = list(query.lower())
    key = list(key.lower())
    key_len = len(key)
    query_len = len(query)
    sgn = -1 if decrypt else 1

    for i in range(query_len):
        if query[i].isalpha():
            shift = ord(key[i % key_len]) - ord('a')
            query[i] = chr(((ord(query[i]) - ord('a') + shift * sgn) % 26) + ord('a'))

    return ''.join(query)