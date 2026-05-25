nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media =(nota1 + nota2) / 2
if media >= 6.0:
    print("\nAPROVADO. Nota final:", media)
elif  media >= 4:
    print("\nRECUPERAÇÃO. Nota final:", media)
else:                                   # Comentário?
    print("\nREPROVADO. Nota final:", media)
