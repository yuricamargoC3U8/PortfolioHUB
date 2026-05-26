lista_nota = []
while True:
    nota_aluno = float(input("Digite a nota do aluno (Digite [-1] para sair): "))
    if nota_aluno == -1:
        break
    lista_nota.insert(0, nota_aluno)
del lista_nota[-1]
total=sum(lista_nota)
qtd = len(lista_nota)
print("A média aritmética é: ", total / qtd)
print("A quantidade de notas é: ", qtd + 1)