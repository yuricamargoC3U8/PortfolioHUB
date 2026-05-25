menor_valor = 999999999
contador = 0
soma = 0
# menor_valor = float('inf')

print("Digite [0] para sair da repetição")
while True:
    valor = int(input("Valor inteiro: "))
    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor
    contador += 1
    soma += valor
print("O menor valor digitado até agora foi: ", menor_valor)
print('A soma dos {} números digitados foram:  {}'.format(contador , soma))
print("A média aritmetica dos valores somados é: ", soma/contador)
