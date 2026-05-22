idade = int(input('Digite a idade do animal: '))
if idade < 4:
    print("Animal Jovem")
elif idade >= 4 and idade < 10:
    print("Animal Adulto")
elif idade >= 10:
    print("Animal idoso")
