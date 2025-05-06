nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))

peso1 = int(input("Digite o primeiro peso:"))
peso2 = int(input("Digite o segundo peso:"))
peso3 = int(input("Digite o terceiro peso:"))

resultado = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print("A média ponderada das notas é:", resultado)