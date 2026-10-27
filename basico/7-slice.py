movie_name = "Top Gun"

# intervalo[aberto:fechado]

# 1 - Buscar toda string a partir da primeira posição
print(movie_name[0:])

# 2 - Buscar toda string até a ultima posição len(movie_name) + 1
print(movie_name[:7])

# 3 - Buscar toda a string a partir da terceira posição
print(movie_name[2:])

"""
string[inicio:fim:passo]
inicio = 0
fim = -1
passo = por padrão é 1

"""

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movie_name[::2])

# 5 - Buscar toda a string nos indices impares
print(movie_name[1::2])

# 6 - Inverter a sstring de tras pra frente
print(movie_name[::-1])