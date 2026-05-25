produtocomprado = str(input("\nDigite seu produto: "))
n1 = float(input("Compra: "))
n2 = float(input("Venda: "))
if n1 > n2:
    print("Teve lucro de:", n1 - n2 )
elif n1 < n2:
    print("Teve Prejuízo de:", n1 - n2)
else:
    print("Valores Iguais!")

if (n1 - n2) > 0:
    print("Você ganhou: ", n1 - n2, produtocomprado)
elif (n1 - n2) < 0:
    print("Você perdeu: ", n1 - n2, produtocomprado)
else:
    print("porra", n1 - n2, produtocomprado)
