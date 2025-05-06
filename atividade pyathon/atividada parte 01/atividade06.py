produto = int(input("valor do produto:"))
desconto = int(input("valor do desconto:"))

resultado = produto * ( desconto / 100 )
r = produto - resultado
print("desconto é:" , r) 