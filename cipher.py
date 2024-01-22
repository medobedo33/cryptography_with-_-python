"""
Descriotion: Caser cipher implementation
author MO TAREK 
"""


# INPUT
plaintext = input("enter the plaintext:")
key = int(input("enter the key:"))
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJklMnOQRSTUVWXYZ"
# PROCESS


def ceaser_encrypt(plaintext: str, key: int):
    plaintext = plaintext.lower()
    ciphertext = ""
    for letter in plaintext:
        ciphertext += alphabet[(alphabet.index(letter) + key) % 26]
    # ciphertext += chr((ord(letter) + key) % 128)

    return ciphertext


def ceaser_bryteforce():
    return 0


def ceaser_decrypt(ciphertext: str, key: int):
    plaintext = ""
    for letter in ciphertext:
        plaintext += alphabet[(alphabet.index(letter) - key) % 26]
    # ciphertext += chr((ord(letter) - key) % 128)
    return plaintext


# OUTPUT
ciphertext = ceaser_encrypt(plaintext, key)
decrypted = ceaser_decrypt(ciphertext, key)
print("====ceaser Encrytion demo===")
print(f"plaintext: {plaintext}\nciphertext:{ciphertext}")
print(f"decrypted: {decrypted}")

git remote add origin https://github.com/medobedo33/cryptography_with-_-python.git
git branch -M main
git push -u origin main