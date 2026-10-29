"""
1- Escreva um programa que le dois nomes e retorne uma string no formato "Ultimo nome, primeiro nome"
2- Inverta a ordem das palavras em uma string fornecida
3- Verifique se uma string fornecida é um, palindromo (pode ser lida da mesma forma de tras para frente)

"""

# Exercicio 1

name = input("Nome:")
last_name = input("Sobrenome:")
print(f"{last_name}, {name}")

# Exercício 2

text = "Python é muito interessante"
words = text.split()

# concatena os elementos de uma lista em uma unica string
inverted_text = " ".join(words[::-1])

print(inverted_text)

# Exercicio 3

palindromo = input("Palavra:")
print(palindromo)
print(palindromo[::-1])

if(palindromo[::1] == palindromo[::-1]):
    print("É Palindromo")
else:
    print("Não é palindromo")