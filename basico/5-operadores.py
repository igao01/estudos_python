num1 = int(input("Numero: "))
num2 = int(input("Numero: "))

# Aristméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma: {sum}\n"
      f"Subtração: {sub}\n"
      f"Divisão: {div}\n"
      f"Multiplicação: {mult}\n"
      f"Módulo: {mod}\n"
      f"{num1} elevado a {num2} é: {exp}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"{num1} e {num2} são iguais? {equal}")
print(f"{num1} e maior que {num2} ? {bigger}")

# Atribuição
num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1