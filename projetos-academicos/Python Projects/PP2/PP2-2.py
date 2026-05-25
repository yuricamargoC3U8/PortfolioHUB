counter = 0
sum = 0
print('Digite [-1] para sair ')
while True:
    number = float(input('Digite um numero: '))
    if number == -1:
        break
    counter += 1
    sum += number
print("A quantidade de numeros que voce digitou foi: ", counter)
print("A soma dos numeros que você digitou foi: ", sum)
print("A média aritmética de todos os valores foi: ", sum / counter)
if  sum >= 20:
    print("A quantidade de valores excede 20")
else:
    print("A quantidade de valores não excede 20")
