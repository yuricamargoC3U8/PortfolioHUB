aprovados = 0
reprovados = 0
print("Digite -1 para sair do programa.")
while True:
    nota = float(input("Informe a nota do aluno: "))
    if nota == -1:
        break
    if nota >= 5:
        aprovados += 1
    else:
        reprovados += 1
    soma_nota = 0
    soma_nota += nota
    total_alunos = aprovados + reprovados
print("A quantidade de alunos que realizaram a prova foi: ", total_alunos)
print("A quantidade de alunos que foram aprovados foi: ", aprovados)
print("A quantidade de alunos que foram reprovados foi: ", reprovados)
print("A média aritmética da nota dos alunos da turma foi: ", soma_nota / total_alunos)
