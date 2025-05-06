valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))

print("Antes da troca:")
print("valor1 =", valor1)
print("valor2 =", valor2)

valor1, valor2 = valor2, valor1

print("Depois da troca:")
print("valor1 =", valor1)
print("valor2 =", valor2)