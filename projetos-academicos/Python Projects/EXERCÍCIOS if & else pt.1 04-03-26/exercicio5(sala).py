print("Mamãe pediu pra comprar 20 vegetais no mercado, não importa quais, apenas leve 20.")
batatas= float(input("Digite o valor de batatas: "))
cenouras= float(input("Digite o valor de cenouras: "))
alface= float(input("Digite o valor de alface: "))

totaldeverduras= batatas+cenouras+alface
print(f"total de verduras é: {totaldeverduras:.0f}")
if totaldeverduras>=20: print("Obrigado meu filho!!")
else:
    print("volta pro mercado pra comprar mais!!")
