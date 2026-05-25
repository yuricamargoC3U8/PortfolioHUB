def positivo_nulo_negativo(number):
    if number > 0:
        print("Valor positivo.")
    elif number < 0:
        print("Valor Negativo")
    else:
        print("Valor Nulo")

def main():
    try:
        valor_digitado = float(input("Digite um numero: "))
        positivo_nulo_negativo(valor_digitado)

    except ValueError:
        print("Erro, insira apenas valores inteiros.")

if __name__ == '__main__':
    main()