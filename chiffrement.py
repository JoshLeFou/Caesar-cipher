import string

# On génère l'alphabet avec la librairie string
alphabet = string.ascii_lowercase
# On transforme notre alphabet en une liste
alphabet = list(alphabet)

# On dédouble la liste
for lettres in range(len(alphabet)):
    alphabet.append(alphabet[lettres])

message = input('Entrez le message à chiffrer : ')
message = message.lower()
print(message)
clef = int(input('Entrez votre clef : '))

# Fonction de chiffrage de césar
def chiffrage(lettre, alphabet, clef):
    for x in range(len(alphabet)):
        if lettre == ' ': # Dans le cas où il y aurait un espace
            return ' '
        elif alphabet[x] == lettre: # Chiffrement avec la clé donnée
            return str(alphabet[x+clef])
    return '?' # Si un caractère inconnu (comme 'é', 'ù', 'à'), afficher '?'
        
message_chiffre = ''

for lettre in message:
    message_chiffre += chiffrage(lettre, alphabet, clef)

print(f'Voici le message chiffré : {message_chiffre}')