# Código SEM datetime -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
nome = str(input("\nDigite seu nome: "))
anonascimento = int(input("Digite o ano de nascimento: "))
if anonascimento <= 2010:
    print("Pode votar meu fi")
else:
    print("Tá um bebe ainda")
print("Seu ano de nascimento é:", anonascimento)
print("Sua idade é: ", 2026 - anonascimento)
print("Seu nome é: ", nome)

# REFACÇÃO DO CODIGO COM DATETIME \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

from datetime import date
nome = str(input("\n\nDigite seu nome: "))
ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
if idade > 16:
    print("Pode votar.")
else:
    print("Novinho ainda,não pode votar")
print("Seu ano de nascimento é: ", ano_nascimento)
print("Sua idade é: ", idade)
print("Seu nome è: ", nome)
