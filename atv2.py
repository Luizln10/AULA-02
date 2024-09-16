idade1 = int(input("Digite a primeira idade: "))
idade2  = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    print(f"{idade1} é maior que {idade2}.")

elif idade1 < idade2:
    print(f"{idade1} é menor que {idade2}.")

else:
    print(f"{idade1} é igual a {idade2}.")