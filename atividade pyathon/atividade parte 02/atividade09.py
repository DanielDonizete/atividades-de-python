valor = float(input("Digite o valor do produto:"))
if valor > 100:
    print("O produto tem desconto")
    desconto = int(input("valor do desconto:"))
    resultado = valor * ( desconto / 100 )
    produto = valor - resultado
    print("desconto é:" , resultado) 
elif valor < 100:
    print("Não tem desconto")
  