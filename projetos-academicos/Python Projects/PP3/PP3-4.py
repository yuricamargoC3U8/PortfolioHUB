salario_minimo = float(input("Digite o valor do salario minimo: "))

abaixo_de_5 = 0
entre_5_e_10 = 0
dez_ou_mais = 0
soma_total = 0

total_funcionarios = int(input("Quantos funcionarios a empresa tem? "))

i = 1
while i <= total_funcionarios:
    salario = float(input("Digite o salario do funcionario: "))

    soma_total = soma_total + salario
    proporcao = salario / salario_minimo

    if proporcao < 5:
        abaixo_de_5 = abaixo_de_5 + 1
    elif proporcao >= 5 and proporcao < 10:
        entre_5_e_10 = entre_5_e_10 + 1
    else:
        dez_ou_mais = dez_ou_mais + 1

    i = i + 1

print("\nRESULTADO FINAL: ")
print("Ganha menos de 5 minimos:", abaixo_de_5)
print("Ganha entre 5 e 10 minimos:", entre_5_e_10)
print("Ganha 10 ou mais minimos:", dez_ou_mais)
print("Valor total da folha: R$", soma_total)
