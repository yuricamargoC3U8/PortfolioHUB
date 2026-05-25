def converte_em_minutos(horas, minutos):
    return (horas * 60) + minutos

def main():
    try:

        hora = int(input('Digite a hora: '))
        minutos = int(input('Digite os minutos: '))
        total1 = converte_em_minutos(hora, minutos)

        hora = int(input('Digite a hora: '))
        minutos = int(input('Digite os minutos: '))
        total2 = converte_em_minutos(hora, minutos)

        print("A diferença entre os horários é de", abs(total1 - total2), "minutos.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros para horas e minutos.")
if __name__ == '__main__':
    main()