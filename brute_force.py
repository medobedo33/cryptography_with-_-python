from cipher import ceaser_decrypt

def ceaser_bruteforce(ciphertext:str):
    for key in range(1,26):
        print(f"{key}: {ceaser_decrypt(ciphertext,key)}")

ciphertext = "khoor"
ceaser_bruteforce(ciphertext)        
