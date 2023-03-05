import random
import string

def generatePassword(length):
    #Define a lista de caracteres permitidos na senha
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #Usa a biblioteca random para criar uma senha aleatória
    password = ''.join(random.choice(characters)for i in range(length))
    
    return password

