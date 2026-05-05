# O problema seria desenvolver um programa que verifique a idade de um indivíduo para que ele possa alugar um veículo dentro da idade legal para alugar.
# **A idade mínima pelas locadoras é 21 apesar de ser legalmente ser 18**
from datetime import datetime
def verificar_aluguel(nome, ano_nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc

    print("Cliente: ", nome)
    print("Idade calculada: ", idade)
    if idade >= 21:
        print("aluguel autorizado.")
    else:
        print(f"Aluguel negado. Faltam {21 - idade} anos para realizar seu aluguel.")
if __name__ == '__main__':
    nome_usuario = input("Digite o nome do cliente: ")
    ano_usuario = int(input("Digite o ano de nascimento (AAAA): "))
    verificar_aluguel(nome_usuario, ano_usuario)
