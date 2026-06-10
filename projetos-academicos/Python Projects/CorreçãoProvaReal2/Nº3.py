lista = []
print("Digite [0] para sair.")
while True:
    valor = int(input("Digite o valor: "))
    if valor == 0:
        break
    lista.append(valor)
print("Maior valor: ", max(lista))
print("Menor valor: ", min(lista))
print("Média: ", sum(lista) / len(lista))
lista[2] = 77
remover = int(input("Digite o valor da remover: "))
lista.remove(remover)