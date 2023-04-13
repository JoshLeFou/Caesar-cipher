import string

alphabet = string.ascii_lowercase
alphabet = list(alphabet)

for lettres in range(len(alphabet)):
    alphabet.append(alphabet[lettres])

message_chiffre = input('Entrez le message à déchiffrer : ')

def chiffrage(lettre, alphabet, clef):
    for x in range(len(alphabet)):
        if lettre == ' ':
            return ' '
        elif alphabet[x] == lettre:
            return str(alphabet[x+clef])
    return '?'

print('Voici les combinaisons possibles :')

for clef in range(1, 26):
    message_dechiffre = ''
    for lettre in message_chiffre:
        message_dechiffre += chiffrage(lettre, alphabet, clef)
    print(f'[*] - {message_dechiffre}')

