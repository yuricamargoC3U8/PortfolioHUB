menor_valor = 99999999999
maior_valor = -99999999999
contador = 0
soma = 0
contador10 = 0

print("Digite [0] para sair da repetição.")
while True:
     valor = int(input("Digite um número inteiro: "))
     if valor == 0:
         break
     if valor > maior_valor:
         maior_valor = valor
     if valor < menor_valor:
         menor_valor = valor
     contador += 1
     soma += valor
     if valor > 10:
         contador10 += 1
print("Quantidade de números maior que 10: ", contador10)
if contador == 0:
    print("Não foi digitado nenhum valor!")
else:
    print("O maior valor digitado foi: ", maior_valor)
    print("O menor valor digitado foi: ", menor_valor)
    print("A soma dos {} numeros digitados é: {}".format(contador, soma))
    print("A média aritmetica da soma dos valores digitados é : ", soma/contador)
