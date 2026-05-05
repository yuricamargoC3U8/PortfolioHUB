qtd_pares = 0
soma_pares = 0

qtd_impares = 0
soma_impares = 0

qtd_total = 0
soma_total = 0

while True:
    num = int(input("Digite um numero(Ou 0 para parar): "))
    if num == 0:
        break
    soma_pares += num
    qtd_total += 1
    if num % 2 == 0:
        soma_pares += num
        qtd_pares += 1
    else:
        soma_impares += num
        qtd_impares += 1
if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
else:
    media_pares = 0

if qtd_impares > 0:
    media_impares = soma_impares / qtd_impares
else:
    media_impares = 0
print("Quantidade total de números digitados: ", qtd_total)
print("Soma total de númmeros digitados: ", soma_total)
print("Média aritmetica dos pares: ", media_pares)
print("Média aritmetica dos impares: ", media_impares)
