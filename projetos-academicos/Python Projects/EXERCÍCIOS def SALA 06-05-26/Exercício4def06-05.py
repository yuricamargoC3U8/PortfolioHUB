def valor_absoluto(v):
    if v < 0:
        vlr_absoluto = -v
    else:
        vlr_absoluto = v
    return vlr_absoluto
def main():
    try:
        valor = float(input("Digite um numero: "))
        retorna = valor_absoluto(valor)
        print("Valor Absoluto: ", retorna)
    except ValueError:
        print("Erro! Digite apenas um número inteiro!")

if __name__ == '__main__':
    main()