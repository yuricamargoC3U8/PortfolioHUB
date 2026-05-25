fahrenheit= float(input("Digite o valor em Fahrenheit: "))
celsius= 5*(fahrenheit-32)/9
print(f"Celsius: {celsius:.0f}")
if celsius >=10: print("POUCO FRIO")
else:
    print("CONGELANDO!!!")
