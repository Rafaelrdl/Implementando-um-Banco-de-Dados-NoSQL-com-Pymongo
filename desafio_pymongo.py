"""
    Módulo desafio_pymongo
    Este módulo tem o objetivo de implementar todo o conhecimento obtido no treinamento com MongoDB.
"""
import datetime
import pprint
import dns
import pymongo as pyM

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']


# Se conecta ao Mongo Atlas
client = pyM.MongoClient("mongodb+srv://rafaelrdlessa:rsxME70F74p5tywZ@cluster0.zp7rz2e.mongodb.net/?retryWrites=true&w=majority")

# cria o DB
db = client.bank

# Cria a coleção 'bank_collection'
collection = db.bank_collection

# Definindo informações para o Doc

information_clients = {
    "Nome": "Rafael Ribeiro",
    "Cpf": 657483920,
    "Endereco": "Belo Horizonte/MG",
    "date": datetime.datetime.utcnow(),
    "Conta": {
        "Tipo": "Conta Corrente",
        "Agencia": "0001",
        "Numero": 237539,
        "Saldo": 345.76
    }
}
# Inserindo o Doc 'information_clientes no DB Bank - Collection clients'
information_clients_bank = db.clients
information_clients_bank_id = information_clients_bank.insert_one(information_clients).inserted_id

# Retorna o ObjectId
print(f"\nObjectId: {information_clients_bank_id}")

# Recuperando informações do doc
print("\nRecuperando todas as informações do Cliente")
pprint.pprint(db.clients.find_one())

# Recuperando informações apenas de Conta

print("\nRecuperando informações atraves da chave e valor ('Nome': 'Rafael Ribeiro').")
pprint.pprint(db.clients.find_one({"Nome": "Rafael Ribeiro"}))

print("\nRecuperando informações atraves da chave e valor ('Cpf': 657483920).")
pprint.pprint(db.clients.find_one({"Cpf": 657483920}))
