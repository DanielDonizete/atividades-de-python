# ATIVIDADE 3: Peça ao usuário para digitar 5 números e calcule a soma deles
contador = 1
soma = 0
while contador <=5:
    # recebendo o número na repetição para não precisar declarar 5 variáveis
    num = int(input("Digite um número: "))
    # somando todo número que o usuário digitar
    soma = soma + num
    # aumentando o contador que dita a quantidade de repetições
    contador = contador + 1
print("A soma é: ",soma)