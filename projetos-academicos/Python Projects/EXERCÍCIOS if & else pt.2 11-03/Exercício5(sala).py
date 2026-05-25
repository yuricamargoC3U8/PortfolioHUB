from datetime import date
nome = str(input("\n\nDigite seu nome: "))
ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
if idade >=18:
    print("Pode votar, CNH permitida.")
elif idade >=16 and idade <18:
    print("Pode votar, CNH não permitida.")
elif idade <16:
    print("Não pode votar, CNH não permitida.")
