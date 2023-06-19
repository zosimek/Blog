import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def generate_fernet_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message

def encrypt_mail_password():
    message = input("Provide the password:").encode("utf-8")
    password = input("Provide the key:").encode("utf-8")
    salt = b'salt'

    key = generate_fernet_key(password, salt)

    encrypted_message = encrypt_message(message, key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

def decrypt_mail_pasword():
    message = input("Provide the encrypted password:").encode("utf-8")
    password = input("Provide the key:").encode("utf-8")

    salt = b'salt'

    key = generate_fernet_key(password, salt)

    original_mail_password = decrypt_message(message, key)
    print(original_mail_password.decode('utf-8'))

# encrypt_mail_password()
decrypt_mail_pasword()