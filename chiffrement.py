import string

alphabet = string.ascii_lowercase
alphabet = list(alphabet)

for lettres in range(len(alphabet)):
    alphabet.append(alphabet[lettres])

message = input('Entrez le message à chiffrer : ')
message = message.lower()
print(message)
clef = int(input('Entrez votre clef : '))

def chiffrage(lettre, alphabet, clef):
    for x in range(len(alphabet)):
        if lettre == ' ':
            return ' '
        elif alphabet[x] == lettre:
            return str(alphabet[x+clef])
    return '?'
        
message_chiffre = ''

for lettre in message:
    message_chiffre += chiffrage(lettre, alphabet, clef)

print(f'Voici le message chiffré : {message_chiffre}')