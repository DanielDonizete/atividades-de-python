#Peça ao usuário para digitar um número e mostre os primeiros números dessa sequência.

quantidade = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

# Os dois primeiros números da sequência
a = 0
b = 1
contador = 0

print("Sequência de Fibonacci:")

while contador < quantidade:
    print(a)
    proximo = a + b
    a = b
    b = proximo
    contador += 1
