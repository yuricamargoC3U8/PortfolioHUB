count = 0
add = 0
num10 = 0
valor_final = int(input("Insira o valor final: "))
for numero in range(0,valor_final+1, 1):
    print(numero)
    print(numero * 2)
    count += 1
    add += numero
    if numero >= 10:
        num10 += 1
print("A quantidade de valores é: ", count)
print("A media é: ", add / count)
print("A qtd de valores maior que 10: ", num10)
print("A soma dos valores é: ", add)
