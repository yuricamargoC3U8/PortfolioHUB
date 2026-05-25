menor_nota = float('inf')
maior_nota = float('-inf')
reprovados = 0
count = 0
add = 0
while True:
    nota = float(input("Digite a nota (digite -1 para parar): "))
    if nota == -1:
        break
    count += 1
    add += nota
    if nota < menor_nota:
        menor_nota = nota
    elif nota > maior_nota:
        maior_nota = nota

    if nota < 5:
        reprovados += 1
print("A quantidade de notas que voce digitou foi: ", count)
print("A soma das notas foi: ", add)
print("A média é: ", add / count)
print("A menor nota foi: ", menor_nota)
print("A maior nota foi: ", maior_nota)
print("A qtd de reprovados foi: ", reprovados)
