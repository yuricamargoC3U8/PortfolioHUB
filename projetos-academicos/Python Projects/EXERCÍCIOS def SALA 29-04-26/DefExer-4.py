def soma(v1, v2):
    somada = v1 + v2
    return somada
def subtrai(v1, v2):
    subtracao = v1 - v2
    return subtracao
if __name__ == '__main__':
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite um valor: '))
    opcao = int(input('Digite uma opcao [1] soma [2] subtrair: '))
    if opcao == 1:
        print(soma(num1, num2))
    elif opcao == 2:
        print(subtrai(num1, num2))
    else:
        print('Opcao invalida')
