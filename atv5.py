nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 > 6 and nota2 > 6:
    print(f"A nota {nota1} é maior que 6!")
    print(f"A nota {nota2} é maior que 6!")

elif nota1 == 6 and nota2 == 6:
     print(f"A nota {nota1} é igual a 6!")
     print(f"A nota {nota2} é igual a 6!")
else:
    print(f"A nota {nota1} não é maior que 6!")
    print(f"A nota {nota2} não é maior que 6!")