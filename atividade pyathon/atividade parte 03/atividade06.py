#Pense em um número e faça com que o usuário adivinhe até acertar. Forneça dicas se o palpite for muito alto ou muito baixo.

import random

# Escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

while True:
    palpite = int(input("Seu palpite: "))
    
    if palpite < numero_secreto:
        print("Muito baixo. Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto. Tente novamente.")
    else:
        print("Parabéns! Você acertou!")
        break
