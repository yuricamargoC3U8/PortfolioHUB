def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
def main():
    numero = int(input("Digite um numero: "))
    fatorial(numero)
    print(fatorial(numero))
if __name__ == "__main__":
    main()
