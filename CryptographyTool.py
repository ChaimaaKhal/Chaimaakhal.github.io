from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Define encryption and decryption functions
def encrypt_message(message, key):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(key))
    cipher = Cipher(algorithms.AES(derived_key), modes.CTR())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return (ciphertext, salt)

def decrypt_message(ciphertext, salt, key):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(key))
    cipher = Cipher(algorithms.AES(derived_key), modes.CTR())
    decryptor = cipher.decryptor()
    message = decryptor.update(ciphertext) + decryptor.finalize()
    return message

# Generate encryption key
key = os.urandom(32)

# Encrypt message
message = b"my secret message"
ciphertext, salt = encrypt_message(message, key)

# Decrypt message
decrypted_message = decrypt_message(ciphertext, salt, key)

print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypted_message)
