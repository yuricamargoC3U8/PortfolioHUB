soma = 0
for numero in range(1, 500 + 1):
    if numero % 3 == 0 and numero % 2 != 0:
        soma += numero
print(f"Soma: {soma}")
