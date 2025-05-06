#Peça ao usuário para digitar um número e mostre a tabuada desse número (de 1 a 10).
numero = int(input("digite um numero: "))
contador = 1
while contador <=10:
        multiplicaçao = numero * contador
        print(numero, "*", contador, "=",multiplicaçao)
        contador = contador + 1
    