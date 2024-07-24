import urllib.parse

# Meminta input dari pengguna
encoded_query = input("Masukkan string yang di-encode: ")

# Decode URL
decoded_query = urllib.parse.unquote(encoded_query)

print("String yang telah di-decode:")
print(decoded_query)
