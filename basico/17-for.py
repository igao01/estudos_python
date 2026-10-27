# Lista de filmes
movie_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista
for movie in movie_list:
    print(movie)

# 2 - Quando a condição for atendida o Loop será encerrado
for movie in movie_list:
    if movie == "Inception":
        break
    print(movie)

# 3 Quando a condição for atendida o loop vai para a próxima iteração
for movie in movie_list:
    if movie == "Inception":
        continue
    print(movie)

# 4 - Avaliação do filme:
movie_name = input("Digite o nome do filme: \n")
movie_rating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
for i in range(movie_rating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movie_rating > 0:
    average = total / movie_rating
else:
    average = 0

print(f"Média de avaliação do filme {movie_name} é: {average:.2f}")