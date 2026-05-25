from datetime import datetime
def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
if __name__ == '__main__':
    idadeinput = int(input("Digite o seu ano de nascimento: "))
    print(calcular_idade(idadeinput))
