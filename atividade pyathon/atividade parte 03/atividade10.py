#Peça ao usuário para digitar notas até que ele digite um valor negativo. Calcule e mostre a média das notas digitadas

#soma guarda o total das notas
soma = 0
# o contador conta quantas notas foram digitadas
contador = 0
#o while continua pedindo nota ate o usuario digitar uma negativa
while True:
    nota = float(input("Digite uma nova nota(ou valor negativo pra sair): "))
    #se o usuario digitar uma nota negativa para de rodar o codigo
    if nota < 0:
        break
    soma = soma + nota
    #contador + 1 vai contando quantas notas foram digitadas pelo usuario
    contador = contador + 1
    #se tiver pelomenos uma nota valida calcule a media 
    if contador > 0:
        media = soma / contador
        print("A média das notas é: ", media)
    else:
        print("Nenhuma nota valida foi digitada")
