film_vingadores = {
    "title": "Vingadores",
    "yearRelease": 2020,
    "imdbRating": 9.5,
    "genre": ["Sci-fi", "Action", "Heroes"]
}

print(film_vingadores)
print(len(film_vingadores))
print(type(film_vingadores))

# 1 - Recuperar um elemento do dicionario
print(film_vingadores["genre"])
print(film_vingadores.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionario
print(film_vingadores.keys())

# 3 - Buscar apenas os valores do dicionario
print(film_vingadores.values())

# 4 - Buscar itens do dicionario com chave e valor
print(film_vingadores.items())

# 5 - Adicionar itens no dicionario
film_vingadores["director"] = "Christopher Nolan"
print(film_vingadores)

# 6 - Atualizar itens no dicionario
film_vingadores.update({"imdbRating": 9.7})
print(film_vingadores)

# 7 - Remover item do dicionario
film_vingadores.pop("director")
print(film_vingadores) 