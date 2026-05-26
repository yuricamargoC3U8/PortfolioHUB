alturas = []
generos = []

while True:
    altura = float(input("Digite a altura: "))
    if altura == -1:
        break
    genero = input("Digite o genero(m ou f): ").strip().lower()

    alturas.append(altura)
    generos.append(genero)

if len(alturas) > 0:
    maior_altura = max(alturas)
    menor_altura = min(alturas)

    qtd_homens = generos.count('m')
    qtd_mulheres = generos.count('f')

    print(f"Maior altura: {maior_altura}m")
    print(f"Menor altura: {menor_altura}m")
    print(f"Quantidade de homens: {qtd_homens}")
    print(f"Quantidade de mulheres: {qtd_mulheres}")
else:
    print("Valor inválido")
