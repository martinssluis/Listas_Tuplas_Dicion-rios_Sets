# Coleções são variáveis que conseguem armazenar vários tipos de dados

# Exemplo de lista (ordenada e mutável)
lista = ["Luffy", True, 11, 0.65]
print("Lista:")
print(lista)
print(f"Tipo: {type(lista)}")
print('#' * 25)  # Divisor

# Imprimir os elementos da lista separadamente
for item in lista:
    print(item)

# Exemplo de tupla (ordenada e imutável)
tupla = ("Zoro", True, 11, 0.65)
print("\nTupla:")
print(tupla)
print(f"Tipo: {type(tupla)}")
print('#' * 25)  # Divisor

# Imprimir os elementos da tupla separadamente
for item in tupla:
    print(item)

# Exemplo de dicionário (ordenado e mutável, sem membros duplicados)
dicionario = {
    "nome": "Sanji",  # Chave: nome, Valor: Sanji
    "Booleano": True, # Chave: Booleano, Valor: True
    "Inteiro": 11,    # Chave: Inteiro, Valor: 11
    "Float": 0.65     # Chave: Float, Valor: 0.65
}

print("\nDicionário:")
print(dicionario)
print(f"Tipo: {type(dicionario)}")
print('#' * 25)  # Divisor

# Imprimir as chaves do dicionário
for chave in dicionario:
    print(chave)

# Exemplo de conjunto (não ordenado e sem índices, sem membros duplicados)
conjunto = {"Nami", True, 11, 0.65}
print("\nConjunto:")
print(conjunto)
print(f"Tipo: {type(conjunto)}")
print('#' * 25)  # Divisor

# Imprimir os elementos do conjunto
for item in conjunto:
    print(item)
