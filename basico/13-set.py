films_set = {"Matrix", "Vingadores", "Dead Pool", "Convergente", "Troia"}
print(type(films_set))

# 1 - Tamanho do set
print(len(films_set))

# 2 - True e 1 são considerados o mesmo valor
example_set = {"Vingadores", True, 1, 8.7}
print(example_set)

# 3 Adiciona item de outro set (faz junção dos dois mantendo somente 1 valor caso tenha duplicidades)
films_set.update(example_set)
print(films_set)

# 4 - Remove um item no set
films_set.remove(True)
films_set.remove(8.7)
print(films_set)