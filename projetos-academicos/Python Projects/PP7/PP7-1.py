lista = []
while True:
    numeros = int(input('Digite vários números (-1 para parar): '))
    if numeros == -1:
        break
    lista.append(numeros)
qtd = len(lista)
print("Quantidade: ", qtd)
