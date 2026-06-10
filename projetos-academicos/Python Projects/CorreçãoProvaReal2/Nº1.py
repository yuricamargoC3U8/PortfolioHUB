soma_pesos = 0
ct_geral = 0
mais_magra = 200
soma_peso_50 = 0
ct_50 = 0
mais_gorda = 0
for i in range(1,5+1):
    peso = float(input("Digite o peso das pessoa: "))
    soma_pesos += peso
    ct_geral += 1
    if peso >= 50:
        ct_50 += 1
        soma_peso_50 += peso
    if peso < mais_magra:
        mais_magra = peso
    if peso > mais_gorda:
        mais_gorda = peso
media = soma_pesos / ct_geral
media_50 = soma_peso_50 / ct_50
print("Média aritmética: ", media)
print("Média dos gordos: ", media_50)
print("Peso da pessoa mais magra: ", mais_magra)
print("Quantidade de pessoas com 50kg ou mais: ", ct_50)
print("Quantidade de pessoas: ", ct_geral)