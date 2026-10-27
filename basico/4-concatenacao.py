name = input("Informe o nome do filme: \n")
year_launch = int(input("Ano de lançamento: \n"))
score = float(input("Nota do filme: \n"))

print("Dados do filme")
print("=====================")

# Alternativa 1
print("Nome do filme:", name, "\nAno de Lançamento:", year_launch, "\nNota:", score)

# Alternativa 2
print(f"Nome do filme: {name} \n"
      f"Ano de Lançamento: {year_launch} \n"
      f"Nota: {score}")