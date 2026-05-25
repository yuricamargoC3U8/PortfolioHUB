contador_masculino = 0
contador_feminino = 0
maior = 0
menor = 3
print("Digite [0] para sair.")
while True:
    altura = float(input("Altura: "))
    if altura == 0:
        break
    genero = str(input("Genero M para masculino, F para feminino: "))
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura
    if genero == "M":
        contador_masculino += 1
    elif genero == "F":
        contador_feminino += 1
    else:
        print("Genero invalido")
print("Maior altuyra: ", maior)
print("Menor altura: ", menor)
print("Quantidade de homens: ", contador_masculino)
print("Quantidade de mulheres: ", contador_feminino)
