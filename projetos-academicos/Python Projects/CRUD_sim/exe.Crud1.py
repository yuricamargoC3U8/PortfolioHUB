lista_nomes = []

def create():
    while True:
        nome_digitado = str(input("Digite um nome ([stop] para parar o programa): "))
        if nome_digitado == "stop":
            break
        lista_nomes.append(nome_digitado)
def read():
    if lista_nomes == []:
        print("Lista Vazia...")
    else:
        for nome in lista_nomes:
            print(nome)
def update():
    if lista_nomes == []:
        print("Lista Vazia...")
    else:
        novo_nome = str(input("Digite um novo nome (stop para parar o programa): "))
        indice = int(input("Digite o indice (stop para parar o programa): "))
        lista_nomes[indice] = novo_nome
def delete():
    indice = int(input("Digite o indice para deletar um nome(stop para parar o programa): "))
    lista_nomes.pop(indice)
    print(lista_nomes)
if __name__ == "__main__":
    while True:
        opcao = str(input("Menu de Opções:\n[C] - Create\n[R] - Read\n[U] - Update\n[D] - Delete\n[E] - Exit\n"))
        if opcao == "C" or opcao == "c":
            create()
        elif opcao == "R" or opcao == "r":
            read()
        elif opcao == "U" or opcao == "u":
            update()
        elif opcao == "D" or opcao == "d":
            delete()
        elif opcao == "E" or opcao == "e":
            print(lista_nomes)
            break
        else:
            print("Opção Inválida! Voltando...")