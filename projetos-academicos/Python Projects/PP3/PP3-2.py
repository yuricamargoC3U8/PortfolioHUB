maior_valor = -9999999999999
menor_valor = 9999999999999
counter = 0
add = 0
add50 = 0
while True:
    valor = int(input("Digite um valor (0 para sair): "))

    if valor == 0:
        break
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor
    counter += 1
    add += valor
    if valor >= 50:
        add50 += 1
print("\nRESULTADOS: ")
print("A quantidade de valores digitados foi: ", counter)
print("A soma dos valores digitados foi: ", add)
print("A média aritmética dos valores foi: ", add / counter)
print("O maior valor digitado foi: ", maior_valor)
print("O menor valor digitado foi: ", menor_valor)
print("A quantidade de valores digitados maior que 50 foi: ", add50)


# 2. Desenvolva o programa que leia vários valores reais
# e no final mostre as seguintes
# informações:
# A quantidade de valores digitados;
# A soma dos valores digitados;
# A média aritmética dos valores digitados;
# O maior valor digitado;
# O menor valor digitado;
# E a quantidade de valores digitados maior ou igual a 50.
