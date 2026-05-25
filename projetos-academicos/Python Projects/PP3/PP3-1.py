add_par = 0
qtd_par = 0
add_impar = 0
qtd_impar = 0

qtd_total = 0
add_total = 0
while True:
    numero = int(input("Digite seu número (0 para sair): "))
    if numero == 0:
        break
    qtd_total += 1
    add_total += numero

    if numero % 2 == 0:
        add_par += numero
        qtd_par += 1
    else:
        add_impar += numero
        qtd_impar += 1
if qtd_par > 0:
    media_par = add_par / qtd_par
else:
    media_par = 0
if qtd_impar > 0:
    media_impar = add_impar / qtd_impar
else:
    media_impar = 0
print("\nRESULTADOS: ")
print("A quantidade de números que você digitou foi: ", qtd_total)
print("A soma dos números que você digitou foi: ", add_total)
print("A média total dos números pares é: ", media_par)
print("A média total de números impares é: ", media_impar)

# 1.	Construa o programa que calcule a média aritmética dos números pares e a média aritmética
# dos números ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualquer
# par ou ímpar. A condição de saída será o número 0 (zero).
# Na tela de saída, mostre também a quantidade total de números digitados e a soma total de
# números digitados.
