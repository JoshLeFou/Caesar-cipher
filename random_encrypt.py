import string
import random

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Entrez le message à chiffrer : ")
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"message original : {plain_text}")
print(f"message crypté : {cipher_text}")

# DECRYPT
cipher_text = plain_text = input("Entrez le message à déchiffrer : ")
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"message original : {cipher_text}")
print(f"message décrypté : {plain_text}")