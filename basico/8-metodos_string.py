movie_name = "Top Gun"
movie_description = """
    Top Gun Maverick, é um filme de ação e aventura,
muito consagrado na indústria.
"""

print(movie_name.upper()) # Tudo maiúsculo
print(movie_name.lower()) # Tudo minúsculo
print(movie_name.capitalize()) # Primeira letra maiúscula
print(movie_name.title()) # Primeira letra de cada palavra maiúscula

# Retorna a string centralizada com caractere de prreenchimento
print(movie_name.center(10, "-"))

# Retorna index do caracteres
print(movie_name.find("u"))

# Retorna a contagem do caracter presente na string
print(movie_name.count("G"))

# Altera um elemento por outro
print(movie_name.replace("Top", "Matrix")) 

print(movie_description.split(','))