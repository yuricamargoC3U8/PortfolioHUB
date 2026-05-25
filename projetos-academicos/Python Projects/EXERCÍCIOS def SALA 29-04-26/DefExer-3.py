def soma(v1, v2):
    somada = v1 + v2
    return somada
def subtrai(v1, v2):
    subtracao = v1 - v2
    return subtracao
if __name__ == '__main__':
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite um valor: '))
    print (soma(num1, num2))
    print (subtrai(num1, num2))
