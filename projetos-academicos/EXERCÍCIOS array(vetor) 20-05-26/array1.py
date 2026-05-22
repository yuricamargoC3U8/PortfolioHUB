lista1 = []
contador = 0
while True:
    numeros = int(input("Digite 10 números para inserir na lista: "))
    if contador == 10:
        break
    lista1.append(numeros)
    contador += 1
# Inserir número no index;
lista1.insert(2, 33)
print(lista1)
# Mostra a lista;
print(lista1)
# Mostra a lista em horizontal;
for item in lista1:
    print(item)
# Mostra a quantidade de numeros na lista;
qtd = len(lista1)
print("quantidade: ", qtd)
# Mostra a soma dos numeros na lista;
sum = sum(lista1)
print("soma: ", sum)
# Mostra o maior valor da lista;
print("Maior valor: ", max(lista1))
# Mostra o menos valor da lista;
print("Menor valor: ", min(lista1))
# Procura se um número está dentro da lista;
pesquisa = int(input("Digite um número para ver se está na lista: "))
if pesquisa in lista1:
    print("Válido")
else:
    print("Inválido")
# Procura o lugar (index) do número digitado na pesquisa;
if pesquisa in lista1:
    print("O índice do número é: ", lista1.index(pesquisa))
else:
    print("Valor não encontrado.")
# Ordem Crescente:
lista1.sort()
print(lista1)
