

nomes = ['Alice', 'Samuel', 'Emily', 'Sofia']
print(nomes[2])
print(nomes[0])


lista1 = [3, 'abacate', 9.7, [5,6,7], "Python", (3,'j')]
print(lista1[2])
print(lista1[0])
print(lista1[3][1])         # Pega o valor do colchetes (se tiver colchetes dentro de um array) em ordem.

pesquisa = float(input("Digite o valor da pesquisa: "))
if pesquisa in lista1:
    print("Valor está na lista")
else:
    print("Valor não está na lista")