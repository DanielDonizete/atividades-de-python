#Solicite um número ao usuário e verifique se ele é primo ou não. 
numero = int(input("Digite um numero para saber se é primo ou não: "))
mult = 0
for c in range(2,numero-1):
    if (numero % c == 0):
        print("Multiplo de ",c)
    mult = mult + 1
if (mult==0):
    print(numero,"É primo porque e divisivel por 1 e por ele mesmo")
else:
    print("Não e primo Tem {} multiplos acima de 2 e abaixo de {}" .format(mult, numero))
