n1= float(input("Digite o valor: "))
n2= float(input("Digite o valor: "))
opcao= int(input("[1] - Somar\n[2] - Subtrair\nDigite uma operação: "))
if opcao ==1:
    soma = n1 + n2
    print(f"\nSoma: {soma:.0f}")
else:
    subtrai = n1 - n2
    print(f"\nSoma: {subtrai:.0f}")
