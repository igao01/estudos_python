films_tuple = ("Matrix", "Vingadores", "Dead Pool", "Convergente", "Troia")
print(type(films_tuple))

# 1 - Buscar os dois primeiros da lista
print(films_tuple[:2])

# 2 - Buscar o ultimo item da lista
print(films_tuple[-1])

# 3 - Buscar filmes até uma determinada posição
print(films_tuple[:3])

# 4 - Buscar filmes de uma pósição em diante
print(films_tuple[1:4])

# 5 - Recuperar o index de um item da tupla
print(films_tuple.index("Vingadores"))