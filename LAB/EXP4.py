# LAB 4: VPN Confidentiality Using a Simple Stream Cipher
# Aim: Demonstrate how encrypted data becomes unreadable without the shared key.


def encrypt(message, key):
    result = ""
    for i in range(len(message)):
        result += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return result


message = "Hello VPN"
key = "KEY"
encrypted = encrypt(message, key)
print("Original Message:", message)
print("Encrypted Message:", encrypted)

decrypted = encrypt(encrypted, key)
print("Decrypted Message:", decrypted)

wrong_key = "BAD"
wrong_decryption = encrypt(encrypted, wrong_key)
print("Using Wrong Key:", wrong_decryption)
