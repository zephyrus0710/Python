

text = input("Enter text: ")
key = int(input("Enter key: "))

encrypted = ""
for char in text:
    encrypted += chr(ord(char) + key)

print("Encrypted:", encrypted)


decrypted = ""
for char in encrypted:
    decrypted += chr(ord(char) - key)

print("Decrypted:", decrypted)



