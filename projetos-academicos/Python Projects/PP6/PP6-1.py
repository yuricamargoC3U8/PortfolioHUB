def soma(x,y):
    soma = x + y
    print(soma)
def subtrair(x,y):
    subtrair = x - y
    print(subtrair)
def multiplicar(x,y):
    multiplicar = x * y
    print(multiplicar)
def dividir(x,y):
    dividir = x / y
    print(dividir)

def main():
    try:
        x = int(input("Digite um numero: "))
        operacao = (input("Digite uma operação(+, -, *, /): "))
        y = int(input("Digite outro numero: "))
        if operacao == "+":
            soma(x,y)
        elif operacao == "-":
            subtrair(x,y)
        elif operacao == "*":
            multiplicar(x,y)
        elif operacao == "/":
            dividir(x,y)
        else:
            print("pode nao man")
    except ValueError:
        print("Erro!")
if __name__ == "__main__":
    main()