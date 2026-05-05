voto1 = 0
voto2 = 0
voto3 = 0
nulo4 = 0
branco5 = 0
total = 0

print("1 = candidato 1\n2 = candidato 2\n3 = candidato 3\n4 = nulo\n5 = branco\n0 = sair")
while True:
    voto = int(input("Digite o voto (1, 2, 3, 4, 5 ou 0): "))
    if voto == 0:
        break
    elif voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 4:
        nulo4 += 1
    elif voto == 5:
        branco5 += 1
    else:
        print("Código Inválido!")
        continue
    total += 1
if total > 0:
    porcen_nulo = (nulo4 / total) * 100
    porcen_branco = (branco5 / total) * 100
else:
    porcen_nulo = 0
    porcen_branco = 0

print("\nRESULTADOS: ")
print("votos candidato 1: ", voto1)
print("votos candidato 2: ", voto2)
print("votos candidato 3: ", voto3)
print("Votos nulos: ", nulo4)
print("Votos brancos: ", branco5)
print("Porcentagem de nulos: ", porcen_nulo)
print("Porcentagem de brancos: ", porcen_branco)

# 3.	Em uma eleição presidencial, existem três candidatos. Os votos são informados através de
# código. Os dados utilizados para escrutinagem obedecem à seguinte codificação:
# 1, 2, 3 - voto dos respectivos candidatos;
# 5 - voto nulo;					6 - voto em branco;
# Elabore o programa que calcule o total de votos de cada candidato, total de votos nulos, total
# de votos em branco, percentual de votos nulos e percentual de votos em branco.
