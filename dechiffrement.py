import string

# On génère l'alphabet avec la librairie string
alphabet = string.ascii_lowercase

# On transforme notre alphabet en une liste
alphabet = list(alphabet)

# On dédouble la liste
for lettres in range(len(alphabet)):
    alphabet.append(alphabet[lettres])

message_chiffre = input('Entrez le message à déchiffrer : ')

# Fonction de chiffrage de césar
def chiffrage(lettre, alphabet, clef):
    for x in range(len(alphabet)):
        if lettre == ' ': # Dans le cas où il y aurait un espace
            return ' '
        elif alphabet[x] == lettre: # Chiffrement avec la clé donnée
            return str(alphabet[x+clef])
    return '?' # En cas de caractère inconnu (comme 'é', 'ù', 'à')

print('Voici les combinaisons possibles :')

for clef in range(1, 26):
    message_dechiffre = ''
    for lettre in message_chiffre:
        message_dechiffre += chiffrage(lettre, alphabet, clef)
    print(f'[*] - {message_dechiffre}')

