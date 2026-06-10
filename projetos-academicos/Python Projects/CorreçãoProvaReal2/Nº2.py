def calcula_area_triangulo(base, altura,):
    area = base * altura / 2
    return area
def area_circulo(raio_d):
    area = 3.14 * raio_d ** 2
    return area
if __name__ == '__main__':
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    valor_retorno = calcula_area_triangulo(base, altura)
    print("Area do triangulo: ", valor_retorno)
    raio = float(input("Digite o valor do raio: "))
    print("Area do circulo: ", area_circulo(raio))