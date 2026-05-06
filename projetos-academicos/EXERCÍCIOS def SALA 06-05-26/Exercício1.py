def comparacao(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    return n1
if __name__ == '__main__':
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    resultado = comparacao(n1, n2)
    print(resultado)