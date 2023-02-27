from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

# Initialize Fernet object with key
fernet = Fernet(key)

# Encrypt password
password = "mysecretpassword".encode()
encrypted_password = fernet.encrypt(password)

# Decrypt password
decrypted_password = fernet.decrypt(encrypted_password).decode()

print("Original password:", password)
print("Encrypted password:", encrypted_password)
print("Decrypted password:", decrypted_password)
