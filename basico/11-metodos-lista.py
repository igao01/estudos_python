film_list = ["Matrix", "Vingadores", "Dead Pool", "Convergente", "Troia"]

# 1 - Tamanho da lista
print(len(film_list))

# 2 - Recuperar o index de um item da lista pelo valor
print(film_list.index("Vingadores"))

# 3 - Adicionar item ao final da lista
film_list.append("Mad Max")
print(film_list)

# 4 - Ordenar lista
film_list.sort()
print(film_list)

# 5 - Copiar os itens de uma lista para outra
films_copy = film_list.copy()

# 6 - Remove um item da lista
films_copy.remove("Mad Max")
print(films_copy)

# 7 - Remove todos os itens da lista
film_list.clear()
print(film_list)