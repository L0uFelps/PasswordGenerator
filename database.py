import pymongo
from pymongo import MongoClient
from passGen import *

#estabelece conexão com o banco de dados
client = MongoClient('mongodb://localhost:27017')
db = client['bancoSenha']
collection = db['minhasSenhas']

#Pede para o usuário digitar o tamanho da senha
length = int(input("Digite o tamanho da senha: "))

#gera uma senha aleatória
password = generatePassword(length)

#insere a senha na coleção
doc = {"password": password}
collection.insert_one(doc)

#Exibe a senha que foi gerada
print("A senha gerada é: ", password)