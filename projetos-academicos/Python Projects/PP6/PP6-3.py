# *Desenvolva um programa em Python que utilize uma função para calcular as raízes de uma equação do segundo grau (ax^2 + bx + c = 0). O programa deve seguir os critérios abaixo:*
# 1. Criação da Função: Crie uma função chamada calcular_bhaskara que receba três parâmetros: os coeficientes a, b e c.
# 2 . Cálculo do Delta: Dentro da função, calcule o valor de Delta usando a fórmula: Delta = b^2 - 4ac
# 3. Validações:
#       Se o coeficiente a for igual a zero, a função deve retornar uma mensagem informando que não é uma equação do segundo grau.
#       Se o valor de Delta for negativo, a função deve retornar uma mensagem informando que a equação não possui raízes reais.
# 4. Cálculo das Raízes: Caso as validações passem, a função deve calcular as duas raízes (x1 & x2) utilizando a fórmula de Bhaskara:
#             x = -b +- math.sqrt(Delta) / 2a
import math


def calcular_bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    if a == 0:
        return "O valor de 'a' deve ser diferente de zero."

    if delta < 0:
        return "A equação não possui raízes reais (Delta negativo)."

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2
# Exemplo: a = 1, b = -5, c = 6
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

resultado = calcular_bhaskara(a, b, c)
print(f"Raízes: {resultado}")
