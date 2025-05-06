usuario = int(input("Digite sua idade:"))
#Solicite a idade do usuário e classifique-a em "Criança", "Adolescente", "Adulto Jovem" ou "Adulto". 
if usuario <= 12:
    print("criança")
elif usuario >13 and usuario <17:
    print("Adolecente")
elif usuario >18 and usuario <29:
    print("Adulto jovem")
else:
    print("adulto")

